import inspect
import itertools
import logging
import threading
from collections.abc import Iterator
from queue import PriorityQueue
from typing import NamedTuple, cast

from cob_runtime.interpreter.instance import CobInstance
from cob_runtime.interpreter.thread import CobThread
from cob_runtime.interpreter.types_ import ThreadId
from animation_engine.exceptions import AnimationEngineError

LOG = logging.getLogger(__name__)


class InvalidCobThreadStateError(AnimationEngineError):
    """Raised when a thread is in an invalid state for the current operation."""

    def __init__(self, thread: CobThread):
        self.thread_id = thread.get_id()
        self.state = thread.get_state()

        py_call_stack = inspect.stack()
        # Get the name of the function that called this method
        self.func_name = py_call_stack[1].function if len(py_call_stack) > 1 else "Unknown"
        # Get the class name if available
        if caller := py_call_stack[1].frame.f_locals.get("self", None):
            if clazz := getattr(caller, "__class__"):
                self.func_name = clazz.__name__ + "." + self.func_name

        self.message = (
            f"CobThread #{self.thread_id} is in an invalid state {repr(self.state)} for function {self.func_name}!"
        )
        super().__init__(self.message)


class CobEngine:
    # region Private API
    class __SleepingThread(NamedTuple):
        wake_time: int
        thread_id: ThreadId

    # region Private Members

    __thread_instances: dict[ThreadId, CobThread]
    """ registry of every thread across all CobInstances """
    __tick_added_threads: list[CobThread]
    """ Threads that are added during the tick. """
    __tick_removed_threads: list[ThreadId]
    """ Threads that are removed during the tick. """

    __running_thread_ids: list[ThreadId]
    __waiting_thread_ids: list[ThreadId]

    __sleeping_thread_ids: PriorityQueue[__SleepingThread]

    __current_time: int

    __thread_counter: Iterator[ThreadId]
    _lock: threading.RLock

    # endregion
    # region Private Methods

    def __thread_exists_for_id(self, thread_id: ThreadId) -> bool:
        return thread_id in self.__thread_instances

    def __tick_thread(self, thread: CobThread):
        # keep track of the current running thread in case of errors
        try:
            if thread is not None:
                keep_alive = thread.tick()
                if not keep_alive:
                    self.remove_thread(thread.get_id())
        except AnimationEngineError as err:
            LOG.error("Error in thread #%s for instance %s", thread.get_id(), repr(thread.cob_instance), exc_info=err)
            thread.stop()

    def __wake_sleeping_threads(self):
        while not self.__sleeping_thread_ids.empty():
            sleeping_thread_info = self.__sleeping_thread_ids.get()

            if sleeping_thread_info.wake_time >= self.__current_time:
                # not yet time to wake it up (or any subsequent threads), put it back
                self.__sleeping_thread_ids.put(sleeping_thread_info, block=False)
                return

            thread = self.get_thread(sleeping_thread_info.thread_id)
            match thread.get_state():
                case CobThread.State.Sleep:
                    thread.set_state(CobThread.State.Run)
                    self.__tick_thread(thread)
                case CobThread.State.Dead:
                    self.remove_thread(thread.get_id())
                case _:
                    raise InvalidCobThreadStateError(thread)

    def __tick_running_threads(self):
        """
        Tick all threads that are currently running.
        This is called at the start of each tick.
        :return:
        """

        for thread_id in self.__running_thread_ids:
            self.__tick_thread(self.get_thread(thread_id))

        # threads cannot go from running to running in COB,
        # this means that threads are allowed to create infinite loops
        # and that we must wait for them to somehow yield control
        # Note: If preemption is enabled, this will not be the case
        self.__running_thread_ids.clear()

        # swap running and waiting lists, preparing for next tick
        self.__running_thread_ids, self.__waiting_thread_ids = self.__waiting_thread_ids, self.__running_thread_ids

    # endregion
    # endregion

    # region Public API
    # region Constructor/Destructor
    def __init__(self):
        self.__thread_instances = {}
        self.__tick_added_threads = []
        self.__tick_removed_threads = []

        self.__running_thread_ids = []
        self.__waiting_thread_ids = []

        self.__sleeping_thread_ids = PriorityQueue()
        self.__current_time = 0

        self.__thread_counter = cast(Iterator[ThreadId], itertools.count())

        self._lock = threading.RLock()

    def __del__(self):
        self.__thread_instances.clear()
        self.__tick_added_threads.clear()
        self.__tick_removed_threads.clear()
        self.__running_thread_ids.clear()
        self.__waiting_thread_ids.clear()

        while not self.__sleeping_thread_ids.empty():
            self.__sleeping_thread_ids.get(False)

    # endregion
    # region Public Methods
    def tick(self, delta_time_ms: int):
        self.__current_time += delta_time_ms

        self.__tick_running_threads()
        self.process_queued_threads()

        self.__wake_sleeping_threads()
        self.process_queued_threads()

    def get_thread(self, thread_id: ThreadId) -> CobThread | None:
        return self.__thread_instances.get(thread_id, None)

    def generate_thread_id(self) -> ThreadId:
        return next(self.__thread_counter)

    def add_thread(self, thread: CobThread) -> ThreadId:
        if (t_id := (thread.get_id() or -1)) < 0:
            t_id = self.generate_thread_id()
            thread.set_id(t_id)

        if t_id in self.__thread_instances:
            raise AnimationEngineError(f"Thread #{t_id} has already been added!")

        self.__thread_instances[t_id] = thread

        instance = thread.cob_instance
        instance.register_thread_id(t_id, thread)

        return t_id

    def remove_thread(self, thread_id: ThreadId) -> bool:
        if thread_id in self.__thread_instances:
            if (thread := self.__thread_instances[thread_id]) is not None and not thread.is_dead():
                thread.stop()
            del self.__thread_instances[thread_id]
            return True
        return False

    def queue_add_thread(self, thread: CobThread):
        """Queue a thread to be added inbetween ticks."""
        self.__tick_added_threads.append(thread)

    def queue_remove_thread(self, thread_id: ThreadId):
        """Queue a thread to be removed inbetween ticks."""
        self.__tick_removed_threads.append(thread_id)

    def process_queued_threads(self):
        """
        Process threads that have been added or removed during the tick.
        Happens twice per tick, once just after all running threads have been ticked,
        and once after all sleeping threads have been woken up and ticked.
        """

        for thread_id in self.__tick_removed_threads:
            self.remove_thread(thread_id)
        self.__tick_removed_threads.clear()

        for thread in self.__tick_added_threads:
            self.add_thread(thread)
        self.__tick_added_threads.clear()

    def assert_no_threads_for_instance(self, instance: CobInstance) -> None:
        """
        Assert that there are no threads running or waiting to run for the given instance.
        This is used to sanity check that the engine is not holding onto threads that should've been destroyed.
        :param instance:
        """

        for thread in self.__thread_instances.values():
            if thread.cob_instance == instance:
                raise AnimationEngineError(
                    f"Thread #{thread.get_id()} for instance {repr(instance)}"
                    f" should have been destroyed, but is still running!"
                )

        for thread in self.__tick_added_threads:
            if thread.cob_instance == instance:
                raise AnimationEngineError(
                    f"Thread #{thread.get_id()} for instance {repr(instance)}"
                    f" should have been destroyed, but is still queued to be added!"
                )

    def schedule_thread(self, thread: CobThread):
        match thread.get_state():
            case CobThread.State.Run:
                self.__waiting_thread_ids.append(thread.get_id())
            case CobThread.State.Sleep:
                self.__sleeping_thread_ids.put(
                    self.__SleepingThread(thread.get_wake_time(), thread.get_id()), block=False
                )
            case _:
                raise InvalidCobThreadStateError(thread)
