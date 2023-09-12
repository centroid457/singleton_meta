import os
import pytest
import pathlib
import shutil
from tempfile import TemporaryDirectory
from typing import *
import threading

from singleton_meta import *


# =====================================================================================================================
def test__nesting_direct():
    class Victim(Singleton):
        attr = 1

    class Victim2(Singleton):
        attr = 11

    assert Victim().attr == 1
    Victim().attr = 2
    assert Victim().attr == 2

    assert Victim2().attr == 11
    Victim2().attr = 22
    assert Victim2().attr == 22

    assert Victim().attr == 2


def test__nesting_several():
    class Victim(Singleton):
        attr = 1
    class Victim2(Victim):
        attr = 11

    assert Victim().attr == 1
    Victim().attr = 2
    assert Victim().attr == 2

    # TRY USE SECOND LEVEL NESTING - ALL WRONG! dont use several levels!!!
    assert Victim2().attr == 2  # UNEXPECTED!

    class Victim2(Victim, metaclass=SingletonMeta):
        attr = 11
    assert Victim2().attr == 2  # UNEXPECTED!



# =====================================================================================================================
