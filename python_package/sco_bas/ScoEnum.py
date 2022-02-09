#!/usr/bin/python3
# coding: UTF-8


# enum.py
from enum import \
    Enum

# typing.py
from typing import \
    Type, \
    Any, \
    Final

class ScoEnum(Enum):

    def __new__(cls: Type, *args: tuple) -> Any:

        zbi: Final[int] = len(cls.__members__)
        self = object.__new__(cls)

        if (len(args) == 1):
            self._value_ = args[0]
        else:
            self._value_ = args

        self.zbi = zbi

        return self


    def __init__(self, *args: tuple) -> None:

        self.zbi: int

