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
@pytest.mark.parametrize(argnames="VictimBase", argvalues=[SingletonByCallMeta, SingletonByNew])
def test__no_args(VictimBase):
    class Victim1(VictimBase):
        attr = 1

    class Victim2(VictimBase):
        attr = 2

    VictimBase._drop_all()
    assert VictimBase._SINGLETONS == []

    assert Victim1().attr == 1
    Victim1().attr = 11
    assert Victim1().attr == 11
    assert VictimBase._SINGLETONS == [Victim1(), ]

    assert Victim2().attr == 2
    Victim2().attr = 22
    assert Victim2().attr == 22
    assert VictimBase._SINGLETONS == [Victim1(), Victim2()]

    assert Victim1().attr == 11

def test__META_with_args():
    VictimBase = SingletonByCallMeta
    VictimBase._SINGLETONS = []
    class Victim1(VictimBase):
        def __init__(self, attr):
            self.attr = attr

    assert VictimBase._SINGLETONS == []
    instance = Victim1(1)

    assert instance.attr == 1
    assert Victim1(111).attr == 1
    assert VictimBase._SINGLETONS == [instance, ]

    Victim1(111).attr = 11
    assert Victim1(1).attr == 11
    assert VictimBase._SINGLETONS == [instance, ]

    assert Victim1(1111).attr == 11
    assert VictimBase._SINGLETONS == [instance, ]

def test__NoMETA_with_args():
    VictimBase = SingletonByNew
    VictimBase._SINGLETONS = []
    class Victim1(VictimBase):
        def __init__(self, attr):
            self.attr = attr

    assert VictimBase._SINGLETONS == []
    instance = Victim1(1)

    assert instance.attr == 1
    assert Victim1(111).attr == 111
    assert VictimBase._SINGLETONS == [instance, ]

    assert Victim1(1).attr == 1
    assert VictimBase._SINGLETONS == [instance, ]

def test__nesting_else_one_meta():
    # cant use else one metaclass in nesting!
    try:
        class Victim1(SingletonByCallMeta, abc.ABC):
            attr = 1
    except TypeError:
        msg = """
        TypeError: metaclass conflict: the metaclass of a derived class must be a (non-strict) subclass of the metaclasses of all its bases

        """
        pass
    else:
        assert False

    class Victim2(SingletonByNew, abc.ABC):
        attr = 2
    assert Victim2().attr == 2
    Victim2().attr = 22
    assert Victim2().attr == 22

def test__threading_spawn():
    class Victim1(SingletonByCallMeta):
        def __init__(self):
            time.sleep(1)

    threads = []
    for item in range(10):
        threads.append(threading.Thread(target=Victim1))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
        assert thread.is_alive() is False

def test__several_levels_at_ones__low():
    VictimBase = SingletonByCallMeta
    class VictimBase2(VictimBase):
        attr = 0
    class Victim1(VictimBase2):
        attr = 1
    class Victim2(VictimBase2):
        attr = 2

    assert VictimBase2().attr == 0
    try:
        assert Victim1().attr == 1
    except Exx_SingletonNestingLevels:
        pass
    else:
        assert False


def test__several_levels_at_ones__up():
    VictimBase = SingletonByCallMeta

    class VictimBase2(VictimBase):
        attr = 0

    class Victim1(VictimBase2):
        attr = 1

    class Victim2(VictimBase2):
        attr = 2

    assert Victim1().attr == 1
    assert Victim2().attr == 2
    try:
        assert VictimBase2().attr == 0
    except Exx_SingletonNestingLevels:
        pass
    else:
        assert False


# =====================================================================================================================
