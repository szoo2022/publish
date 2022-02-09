#!/usr/bin/python3
# coding: UTF-8


# typing.py
from typing import \
    Final, \
    Generic, \
    TypeVar

# logging.py
from logging import \
    Logger

# ScoRc.py
from sco_bas.ScoRc import \
    ScoRc

# ScoEnum.py
from sco_bas.ScoEnum import \
    ScoEnum

# sco_log.py
from sco_log.sco_log import \
    sco_log_get


class ScoStubInit(ScoEnum):

    STR: Final[str] = '0x5A5A5A5A'
    INT: Final[int] = 0x5A5A5A5A


T = TypeVar("T")


class ScoStubComs(Generic[T]):

    def __init__(self) -> None:

        self.com_list: Final[list[T]] = []
        self.com_used : int = 0


def ScoStubComs_init(this: ScoStubComs[T]) -> ScoRc:

    log   : Final[Logger] = sco_log_get()
    result: ScoRc = ScoRc.OK

    if (this is not None):
        this.com_list.clear()
        this.com_used = 0
    else:
        result = ScoRc.NG
        log.error('this is None.')

    return result

