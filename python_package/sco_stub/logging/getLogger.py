#!/usr/bin/python3
# coding: UTF-8


# typing.py
from typing import \
    Final, \
    Optional, \
    TypeAlias

# logging.py
from logging import \
    Logger

# sco_log.py
from sco_log.sco_log import \
    sco_log_get

# ScoStubComs.py
from sco_stub.ScoStubComs import \
    ScoStubComs, \
    ScoStubInit

# Logger.py
from .Logger import \
    LoggerStub


class StubCom_getLogger:

    def __init__(self) -> None:

        self.name: str = ScoStubInit.STR 
        self.result: Final[LoggerStub] = LoggerStub()


StubComs_getLogger: TypeAlias = ScoStubComs[StubCom_getLogger]


def getLogger_stub(name: str) -> Optional[Logger]:

    result: Optional[LoggerStub] = None
    coms: Final[StubComs_getLogger] = g_StubComs_getLogger_get()

    if (coms.com_used < len(coms.com_list)):
        com: Final[StubCom_getLogger]= coms.com_list[coms.com_used]
        com.name = name
        result = com.result
        coms.com_used += 1
    else:
        print("getLogger_stub() coms.com_list is short.")

    return result


def g_StubComs_getLogger_get() -> StubComs_getLogger:

    return g_StubComs_getLogger


g_StubComs_getLogger: Final[StubComs_getLogger] = StubComs_getLogger()

