from typing import *
from threading import Lock


# =====================================================================================================================
class Exx_SingletonNestingLevels(Exception):
    """Exception when used several unsuitable levels in nesting!

    EXAMPLE:
        VictimBase = SingletonWMetaCall
        setattr(VictimBase, "attr", 0)
        class Victim1(VictimBase):
            attr = 1

        assert VictimBase().attr == 0
        try:
            assert Victim1().attr == 1
        except Exx_SingletonDifferentNestingLevels:
            pass
        else:
            assert False

    MAIN RULES:
    1. always instantiate only last Classes in your tree project!
    """
    pass


# =====================================================================================================================


# =====================================================================================================================
class SingletonMetaClass(type):
    """metaclass which create the singletons.

    USAGE only like:
        class MySingleton(metaclass=_SingletonMeta):
            pass
    but prefer using SingletonWMetaCall!

    :ivar _mutex_Singleton: mutex for safe creating items
    :ivar _CLS_INST_BLOCKED: set of classes which can NOT be used as singleton! for correct singletons reason!
        if we instantiate one class and then instantiate one of other class nesting this one -
        before you did not understand your architecture mistake, but now it will rase!
        So it prevent and raise incorrect singleton usage
    :ivar _CLS_INST_USED: set of classes which already used as singleton!
    """
    _mutex_Singleton: Lock = Lock()  # keep this special name! dont use just MUTEX! (need uniq! in case of exists in source!)
    _CLS_INST_BLOCKED: Set[Any] = set()
    _CLS_INST_USED: Set[Any] = set()

    def __call__(cls, *args, **kwargs):
        # check blocked --------------------------------------------
        if cls in SingletonMetaClass._CLS_INST_BLOCKED:
            msg = f"{cls.__name__=} WAS BLOCKED before by creating singleton in upper nesting level"
            for cls_blocked in SingletonMetaClass._CLS_INST_BLOCKED:
                msg += f"\n\t{cls_blocked.__name__=}"
            raise Exx_SingletonNestingLevels(msg)

        SingletonMetaClass._CLS_INST_USED.add(cls)

        for cls_mro in cls.__mro__[1:]:
            if cls_mro in SingletonMetaClass._CLS_INST_USED:
                msg = f"{cls.__name__=} WAS USED before by creating singleton in less nesting level"
                for cls_used in SingletonMetaClass._CLS_INST_USED:
                    msg += f"\n\t{cls_used.__name__=}"
                raise Exx_SingletonNestingLevels(msg)
            SingletonMetaClass._CLS_INST_BLOCKED.add(cls_mro)

        # create singleton -----------------------------------------
        cls._mutex_Singleton.acquire()

        cls._mro_check_blocked()

        if not hasattr(cls, '__INSTANCE'):
            setattr(cls, '__INSTANCE', None)
            cls.__INSTANCE = super().__call__(*args, **kwargs)

            # collect from all classes -----------------------------------------
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

    @classmethod
    def _mro_check_blocked(cls) -> Optional[NoReturn]:
        pass


class SingletonWMetaCall(metaclass=SingletonMetaClass):
    """Singleton manager, creating them by using CALL with metaclassing

    :ivar _SINGLETONS: collection of created singletons instances
        when you create several classes, you maybe need to keep access to all of them.
        Used in tests!

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

    # @classmethod
    # def _instance_del(cls) -> None:
    #     """Delete class instance!
    #
    #     expected using for tests!
    #     """
    #     try:
    #         delattr(cls, "__INSTANCE")
    #     except:
    #         pass


class SingletonWoMetaNew:
    """Singleton manager, creating them by using NEW without metaclassing
    else one variant after SingletonWMetaCall, in case of metaclass is not acceptable.

    USEFUL CASES:
    1. you need to use some metaclass (cant set two metaclasses).
    2. always reinit instance on instantiating! (would be called __init__(*args/kwargs)!
        if blank init - will be the same as SingletonWMetaCall

    attributes see in SingletonWMetaCall
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
