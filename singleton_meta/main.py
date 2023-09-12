from threading import Lock


class SingletonMeta(type):
    """
    metaclass which create the singleton logic.
    USE ONLY LIKE
        class MySingleton(metaclass=_SingletonMeta):
            pass
    but prefir use next class Singleton!
    """

    MUTEX: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        cls.MUTEX.acquire()
        if not hasattr(cls, '__INSTANCE'):
            setattr(cls, '__INSTANCE', None)
            cls.__INSTANCE = super().__call__(*args, **kwargs)
        cls.MUTEX.release()
        return cls.__INSTANCE


class Singleton(metaclass=SingletonMeta):
    """
    usable class for typical nesting like
        class MySingleton(Singleton):
            pass
    """
    pass
