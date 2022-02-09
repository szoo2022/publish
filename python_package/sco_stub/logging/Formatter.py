#!/usr/bin/python3
# coding: UTF-8


# typing.py
from typing import \
    Final, \
    TypeAlias, \
    Optional

# logging.py
from logging import \
    Logger, \
    Formatter

# sco_log.py
from sco_log.sco_log import \
    sco_log_get

# ScoStubComs.py
from sco_stub.ScoStubComs import \
    ScoStubInit, \
    ScoStubComs


class FormatterStub(Formatter):

    def __init__(self):

        self.fmt: str = ScoStubInit.STR
        self.ut_id: int = 0


StubComs_Formatter: TypeAlias = ScoStubComs[FormatterStub]


def Formatter_stub(fmt: str) -> Formatter:

    result: Optional[FormatterStub] = None
    log: Final[Logger] = sco_log_get()
    coms: Final[StubComs_Formatter] = g_StubComs_Formatter_get()

    if (coms.com_used < len(coms.com_list)):
        result = coms.com_list[coms.com_used]
        result.fmt = fmt
        coms.com_used += 1
    else:
        log.error("coms.com_list is short.")

    return result


def g_StubComs_Formatter_get() -> StubComs_Formatter:

    return g_StubComs_Formatter


g_StubComs_Formatter: Final[StubComs_Formatter] = StubComs_Formatter()

