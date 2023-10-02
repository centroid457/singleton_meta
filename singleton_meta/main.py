from typing import *
from threading import Lock


# =====================================================================================================================
class SingletonMeta(type):
    """
    metaclass which create the singleton logic.
    USE ONLY LIKE
        class MySingleton(metaclass=_SingletonMeta):
            pass
    but prefer use next class Singleton!

    :param MUTEX: mutex for safe creating items
    """

    MUTEX: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        cls.MUTEX.acquire()
        if not hasattr(cls, '__INSTANCE'):
            setattr(cls, '__INSTANCE', None)
            cls.__INSTANCE = super().__call__(*args, **kwargs)

            # collect from all classes
            if Singleton in cls.__mro__:
                Singleton._SINGLETONS.append(cls.__INSTANCE)

        cls.MUTEX.release()
        return cls.__INSTANCE


class Singleton(metaclass=SingletonMeta):
    """
    usable class for typical nesting like
        class MySingleton(Singleton):
            pass

    :param _SINGLETONS: collection of created singletons instances
        when you create several classes, you maybe need to keep access to all of them.

    USAGE
    -----
    BEST PRACTICE
    Use only one level nesting!
        class Victim1(Singleton):
            pass
        class Victim2(Singleton):
            pass
        class VictimINCORRECT(Victim1):
            pass
    """
    _SINGLETONS: List['Singleton'] = []


# =====================================================================================================================
