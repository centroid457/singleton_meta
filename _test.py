import os
import pytest
import time
import pathlib
import shutil
from tempfile import TemporaryDirectory
from typing import *
import threading
import abc

from singleton_meta import *


# =====================================================================================================================
@pytest.mark.parametrize(argnames="VictimCls", argvalues=[SingletonWMetaCall, SingletonWoMetaNew])
def test__no_args(VictimCls):
    class Victim1(VictimCls):
        attr = 1

    class Victim2(VictimCls):
        attr = 2

    assert VictimCls._SINGLETONS == []

    assert Victim1().attr == 1
    Victim1().attr = 11
    assert Victim1().attr == 11
    assert VictimCls._SINGLETONS == [Victim1(), ]

    assert Victim2().attr == 2
    Victim2().attr = 22
    assert Victim2().attr == 22
    assert VictimCls._SINGLETONS == [Victim1(), Victim2()]

    assert Victim1().attr == 11

def test__META_with_args():
    SingletonWMetaCall._SINGLETONS = []
    class Victim1(SingletonWMetaCall):
        def __init__(self, attr):
            self.attr = attr

    assert SingletonWMetaCall._SINGLETONS == []
    instance = Victim1(1)

    assert instance.attr == 1
    assert Victim1(111).attr == 1
    assert SingletonWMetaCall._SINGLETONS == [instance, ]

    Victim1(111).attr = 11
    assert Victim1(1).attr == 11
    assert SingletonWMetaCall._SINGLETONS == [instance, ]

    assert Victim1(1111).attr == 11
    assert SingletonWMetaCall._SINGLETONS == [instance, ]

def test__NoMETA_with_args():
    SingletonWoMetaNew._SINGLETONS = []
    class Victim1(SingletonWoMetaNew):
        def __init__(self, attr):
            self.attr = attr

    assert SingletonWoMetaNew._SINGLETONS == []
    instance = Victim1(1)

    assert instance.attr == 1
    assert Victim1(111).attr == 111
    assert SingletonWoMetaNew._SINGLETONS == [instance, ]

    assert Victim1(1).attr == 1
    assert SingletonWoMetaNew._SINGLETONS == [instance, ]

def test__nesting_else_one_meta():
    # cant use else one metaclass in nesting!
    try:
        class Victim1(SingletonWMetaCall, abc.ABC):
            attr = 1
    except TypeError:
        msg = """
        TypeError: metaclass conflict: the metaclass of a derived class must be a (non-strict) subclass of the metaclasses of all its bases

        """
        pass
    else:
        assert False

    class Victim2(SingletonWoMetaNew, abc.ABC):
        attr = 2
    assert Victim2().attr == 2
    Victim2().attr = 22
    assert Victim2().attr == 22

def test__threading_spawn():
    def func():
        time.sleep(1)

    threads = []
    for item in range(10):
        threads.append(threading.Thread(target=func))

    for thread in threads:
        thread.start()
        assert thread.is_alive() is True

    for thread in threads:
        thread.join()
        assert thread.is_alive() is False

def test__nesting_INCORRECT():
    class Victim(SingletonWMetaCall):
        attr = 1
    class Victim2(Victim):
        attr = 2

    assert Victim().attr == 1
    Victim().attr = 11
    assert Victim().attr == 11

    # TRY USE SECOND LEVEL NESTING - ALL WRONG! dont use several levels!!!
    assert Victim2().attr == 11  # UNEXPECTED!

    class Victim2(Victim, metaclass=SingletonMetaClass):
        attr = 22
    assert Victim2().attr == 11  # UNEXPECTED!


# =====================================================================================================================
