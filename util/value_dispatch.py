from functools import update_wrapper


class ValueDispatch:
    """ A single-dispatch that can be used as a decorator/descriptor. """
    def __init__(self, func):
        if not callable(func) and not hasattr(func, "__get__"):
            raise TypeError(f"{func!r} is not callable or a descriptor")

        self.dispatch_table = {}
        self.func = func

    def register(self, value):
        def decorator(func):
            if not callable(func) and not hasattr(func, "__get__"):
                raise TypeError(f"{func!r} is not callable or a descriptor")

            self.dispatch_table[value] = func
            return func

        return decorator

    def __get__(self, obj, cls=None):
        def _do_call(call, *args, **kwargs):
            if hasattr(call, '__get__'):
                return call.__get__(obj, cls)(*args, **kwargs)
            return call(*args, **kwargs)

        def _method(value, *args, **kwargs):
            method = self.dispatch_table.get(value, None)
            if method is None:
                return _do_call(self.func, value, *args, **kwargs)
            return _do_call(method, *args, **kwargs)

        _method.register = self.register
        _method.dispatch_table = self.dispatch_table
        update_wrapper(_method, self.func)
        return _method
