#!/usr/bin/python3
# coding: UTF-8


# typing.py
from typing import \
    Final

# enum.py
from enum import \
    auto

# ScoEnum.py
from .ScoEnum import \
    ScoEnum


class ScoEzodfCellSpan(ScoEnum):

    ROW: Final = auto()
    COL: Final = auto()

