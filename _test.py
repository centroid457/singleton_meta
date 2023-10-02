import os
import pytest
import pathlib
import shutil
from tempfile import TemporaryDirectory
from typing import *
import threading

from singleton_meta import *


# =====================================================================================================================
def test__nesting_direct_correct():
    class Victim1(Singleton):
        attr = 1

    class Victim2(Singleton):
        attr = 2

    assert Singleton._SINGLETONS == []

    assert Victim1().attr == 1
    Victim1().attr = 11
    assert Victim1().attr == 11
    assert Singleton._SINGLETONS == [Victim1(), ]

    assert Victim2().attr == 2
    Victim2().attr = 22
    assert Victim2().attr == 22
    assert Victim1().attr == 11
    assert Singleton._SINGLETONS == [Victim1(), Victim2()]


def test__nesting_incorrect():
    class Victim(Singleton):
        attr = 1
    class Victim2(Victim):
        attr = 2

    assert Victim().attr == 1
    Victim().attr = 11
    assert Victim().attr == 11

    # TRY USE SECOND LEVEL NESTING - ALL WRONG! dont use several levels!!!
    assert Victim2().attr == 11  # UNEXPECTED!

    class Victim2(Victim, metaclass=SingletonMeta):
        attr = 22
    assert Victim2().attr == 11  # UNEXPECTED!


# =====================================================================================================================
