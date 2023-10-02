from typing import *
from threading import Lock


# =====================================================================================================================
class SingletonMetaClass(type):
    """
    metaclass which create the singletons.

    USAGE only like:
        class MySingleton(metaclass=_SingletonMeta):
            pass
    but prefer using SingletonWMetaCall!

    :param _mutex_Singleton: mutex for safe creating items
    """
    _mutex_Singleton: Lock = Lock()    # keep this special name! (need uniq! in case of exists in source!)

    def __call__(cls, *args, **kwargs):
        cls._mutex_Singleton.acquire()
        if not hasattr(cls, '__INSTANCE'):
            setattr(cls, '__INSTANCE', None)
            cls.__INSTANCE = super().__call__(*args, **kwargs)

            # collect from all classes
            if SingletonWMetaCall in cls.__mro__:
                if cls.__INSTANCE not in SingletonWMetaCall._SINGLETONS:
                    SingletonWMetaCall._SINGLETONS.append(cls.__INSTANCE)

            # singleton_group_class = cls.__mro__[1]
            # if not hasattr(singleton_group_class, '_INSTANCES'):
            #     setattr(singleton_group_class, '_INSTANCES', [])
            #     singleton_group_class._INSTANCES = []
            # singleton_group_class._INSTANCES.append(cls.__INSTANCE)

        cls._mutex_Singleton.release()
        return cls.__INSTANCE


class SingletonWMetaCall(metaclass=SingletonMetaClass):
    """Singleton manager

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
    _SINGLETONS: List['SingletonWMetaCall'] = []

    # TODO: need clear instance??? maybe for tests?


class SingletonWoMetaNew:
    """else one variant after SingletonWMetaCall.

    USEFUL CASES:
    1. you need to use some metaclass (cant set two metaclasses).
    2. always reinit instance on instantiating! (would be called __init__(*args/kwargs)!
        if blank init - will be the same as SingletonWMetaCall

    params see in SingletonWMetaCall
    """
    _SINGLETONS: List['SingletonWoMetaNew'] = []
    _mutex_Singleton: Lock = Lock()

    def __new__(cls, *args, **kwargs):
        cls._mutex_Singleton.acquire()
        if not hasattr(cls, "__INSTANCE"):
            setattr(cls, "__INSTANCE", None)
            cls.__INSTANCE = super().__new__(cls)

        if SingletonWoMetaNew in cls.__mro__:
            if cls.__INSTANCE not in SingletonWoMetaNew._SINGLETONS:
                SingletonWoMetaNew._SINGLETONS.append(cls.__INSTANCE)

        cls._mutex_Singleton.release()
        return cls.__INSTANCE


# =====================================================================================================================
