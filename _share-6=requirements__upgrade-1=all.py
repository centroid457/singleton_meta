import pathlib
from setuptools import find_packages

from requirements_checker import Packages


# =====================================================================================================================
pkgs_cli = Packages()

pkgs_cli.upgrade_pip()
pkgs_cli.upgrade__centroid457()
pkgs_cli.upgrade(find_packages())

filepath = pathlib.Path(__file__).parent.joinpath("requirements.txt")   # FIXME: not working!
pkgs_cli.upgrade_file(filepath)


# EXIT PAUSE ==========================================================================================================
# for i in range(10, 0, -1):
#     print(f"exit in [{i}] seconds")
#     time.sleep(1)

msg = f"[FINISHED] press Enter to close"
print(msg)
print(msg)
print(msg)
print(msg)
print(msg)
# ---------
input(msg)


# =====================================================================================================================
