#!/usr/bin/python3
# coding: UTF-8


# typing.py
from typing import \
    Final


class ScoOdsRng:

    def __init__(self) -> None:

        self.start : int = 0
        self.length: int = 0


def ScoOdsRng_create(start: int, length: int) -> ScoOdsRng:

    this: Final[ScoOdsRng] = ScoOdsRng()

    this.start  = start
    this.length = length

    return this

