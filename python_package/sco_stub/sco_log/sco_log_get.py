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

# ScoStubComs.py
from sco_stub.ScoStubComs import \
    ScoStubComs

# sco_log.py
from sco_log.sco_log import \
    sco_log_get

# Logger.py
from sco_stub.logging.Logger import \
    LoggerStub


class StubCom_sco_log_get:

    def __init__(self) -> None:

        self.result: Final[LoggerStub] = LoggerStub()


StubComs_sco_log_get: TypeAlias = ScoStubComs[StubCom_sco_log_get]


def sco_log_get_stub() -> Optional[Logger]:

    result: Optional[LoggerStub] = None
    log: Final[Logger] = sco_log_get()
    coms: Final[StubComs_sco_log_get] = g_StubComs_sco_log_get_get()

    if (coms.com_used < len(coms.com_list)):
        com: Final[StubCom_sco_log_get] = coms.com_list[coms.com_used]
        result = com.result
        coms.com_used += 1
    else:
        log.error("coms.com_list is short.")

    return result


def g_StubComs_sco_log_get_get() -> StubComs_sco_log_get:

    return g_StubComs_sco_log_get


g_StubComs_sco_log_get: Final[StubComs_sco_log_get] = StubComs_sco_log_get()

