from typing import *


# =====================================================================================================================
class PROJECT:
    # AUX --------------------------------------------------
    _VERSION_TEMPLATE: Tuple[int] = (0, 0, 1)

    # AUTHOR -----------------------------------------------
    AUTHOR_NAME: str = "Andrei Starichenko"
    AUTHOR_EMAIL: str = "centroid@mail.ru"
    AUTHOR_HOMEPAGE: str = "https://github.com/centroid457/"

    # PROJECT ----------------------------------------------
    NAME_INSTALL: str = "singleton-meta"
    NAME_IMPORT: str = "singleton_meta"
    KEYWORDS: List[str] = [
        "singleton",
        "singleton meta",
        "singleton call",
        "singleton new",
    ]

    # GIT --------------------------------------------------
    DESCRIPTION_SHORT: str = "create perfect singletons"

    # README -----------------------------------------------
    pass

    # add DOUBLE SPACE at the end of all lines! for correct representation in MD-viewers
    DESCRIPTION_LONG: str = """
designed for ...
    """
    FEATURES: List[str] = [
        # "feat1",
        # ["feat2", "block1", "block2"],

        "perfect singleton (maybe thread safe!)",
        "collect all instances",
        "check correct instantiating singletons in tree project",
    ]

    # HISTORY -----------------------------------------------
    VERSION: Tuple[int, int, int] = (0, 1, 1)
    VERSION_STR: str = ".".join(map(str, VERSION))
    TODO: List[str] = [
        "..."
    ]
    FIXME: List[str] = [
        "..."
    ]
    NEWS: List[str] = [
        "apply new pypi template"
    ]


# =====================================================================================================================
if __name__ == '__main__':
    pass


# =====================================================================================================================
