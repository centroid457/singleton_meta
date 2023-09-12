class _SingletonMeta(type):
    """
    metaclass which create the singleton logic.
    USE ONLY LIKE
        class MySingleton(metaclass=_SingletonMeta):
            pass
    but prefir use next class Singleton!
    """
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '__INSTANCE'):
            setattr(cls, '__INSTANCE', None)
            cls.__INSTANCE = super().__call__(*args, **kwargs)
        return cls.__INSTANCE


class Singleton(metaclass=_SingletonMeta):
    """
    usable class for typical nesting like
        class MySingleton(Singleton):
            pass
    """
    pass
