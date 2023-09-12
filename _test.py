import os
import pytest
import pathlib
import shutil
from tempfile import TemporaryDirectory
from typing import *
import threading

from singleton_meta import *


# =====================================================================================================================
def test__simple():
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


# =====================================================================================================================
