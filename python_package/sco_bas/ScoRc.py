#!/usr/bin/env python
# coding: UTF-8


# enum.py
from enum import \
    auto

# typing.py
from typing import \
    Final

# ScoEnum.py
from .ScoEnum import \
    ScoEnum


class ScoRc(ScoEnum):

    OK: Final = auto()
    NG: Final = auto()

