#!/usr/bin/python3
# coding: UTF-8


# typing.py
from typing import \
    Final

# ScoEnum.py
from .ScoEnum import \
    ScoEnum


class ScoEzodfCellValueType(ScoEnum):

    STRING  : Final[str] = "string"
    NUMERIC : Final[str] = "float"
    PERCENT : Final[str] = "percentage"
    CURRENCY: Final[str] = "currency"
    BOOL    : Final[str] = "boolean"
    DATE    : Final[str] = "date"
    TIME    : Final[str] = "time"

