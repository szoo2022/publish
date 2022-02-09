#!/usr/bin/python3
# coding: UTF-8


# typing.py
from typing import \
    Final, \
    Callable, \
    Any


SCO_MODULE_NAME_MAIN: Final[str] = '__main__'

SCO_CB_ANY_T = Callable[[Any], Any]


class Sco_int:

    def __init__(self) -> None:

        self.value: int = 0


class Sco_str:

    def __init__(self) -> None:

        self.value: str = ""


