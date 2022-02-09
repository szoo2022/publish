#!/usr/bin/python3
# coding: UTF-8


# typing.py
from typing import \
    Final

# enum.py
from sco_bas.ScoEnum import \
    ScoEnum


class ScoUtHead(ScoEnum):

    NUMBER: Final[str] = "#"
    INPUT : Final[str] = "Inputs"
    EXPECT: Final[str] = "Expected values of outputs"
    OUTPUT: Final[str] = "Outputs"
    JUDGE : Final[str] = "Judges"

