from concurrent.futures import Future
from concurrent.futures.process import ProcessPoolExecutor

from cob.animation_engine.cob_engine import CobEngine
from cob.animation_engine.unit_script import UnitScript


class UnitScriptEngine:
    __current_script: UnitScript | None
    __animating: list[UnitScript]

    cob_engine: CobEngine | None = None

    # cob_file_handler: CobFileHandler | None = None

    def __init__(self):
        self.__current_script = None
        self.__animating = []

    def add_instance(self, instance: UnitScript) -> None:
        if instance == self.__current_script:
            return

        if instance not in self.__animating:
            self.__animating.append(instance)

    def remove_instance(self, instance: UnitScript) -> None:
        if instance == self.__current_script:
            return

        if instance in self.__animating:
            self.__animating.remove(instance)

    def reload_scripts(self) -> None:
        raise NotImplementedError('TODO, implement reload_scripts')

    def tick(self, delta_time: int) -> None:
        if self.cob_engine:
            self.cob_engine.tick(delta_time)

        self.__tick_multi_threaded(delta_time)
        self.__tick_single_threaded(delta_time)

    def __tick_multi_threaded(self, delta_time: int) -> None:
        with ProcessPoolExecutor() as executor:
            processes: list[Future] = []
            for instance in self.__animating:
                processes.append(executor.submit(instance.tick_all_anims, delta_time))

        errors: list[Exception] = []
        for p in processes:
            try:
                p.result()
            except Exception as e:
                errors.append(e)
        if errors:
            raise ExceptionGroup("Errors occurred during animation tick", errors)

    def __tick_single_threaded(self, delta_time: int) -> None:
        idx = 0
        while idx < len(self.__animating):
            self.__current_script = self.__animating[idx]

            if not self.__current_script.tick_anim_finished(delta_time):
                # If the animation IS finished, remove it by overwriting it with the last animation in the list
                self.__animating[idx] = self.__animating.pop()
                # Do not increment the index, as we need want to process the animation
                # that was just moved to the current index
            else:
                idx += 1
        self.__current_script = None

    def kill(self) -> None:
        self.__animating.clear()
