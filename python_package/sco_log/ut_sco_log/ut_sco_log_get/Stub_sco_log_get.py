#!/usr/bin/python3
# coding: UTF-8


# typing.py
from typing import \
    Final, \
    Callable

# sco_log.py
from sco_log import \
    sco_log

# Spec_sco_log_get.py
from .Spec_sco_log_get import \
    Input_sco_log_get, \
    Expect_sco_log_get

# ScoStubComs.py
from sco_stub.ScoStubComs import \
    ScoStubComs_init

# getLogger.py
from sco_stub.logging.getLogger import \
    StubCom_getLogger, \
    StubComs_getLogger, \
    g_StubComs_getLogger_get, \
    getLogger_stub

# Logger.py
from sco_stub.logging.Logger import \
    LoggerStub


class Stub_sco_log_get:

    def __init__(self) -> None:

        self.result_coms: Final[StubComs_getLogger] = \
            g_StubComs_getLogger_get()
        self.result_src: Callable


def Stub_sco_log_get_set(this: Stub_sco_log_get, set: Input_sco_log_get) \
    -> None:

    result_com: Final[StubCom_getLogger] = StubCom_getLogger()
    result: Final[LoggerStub] = result_com.result
    result.ut_id = set.getLogger_Logger_ut_id
    ScoStubComs_init(this.result_coms)
    this.result_coms.com_list.append(result_com)


def Stub_sco_log_get_get(this: Stub_sco_log_get, get: Expect_sco_log_get) \
    -> None:

    result_com: Final[StubCom_getLogger] = this.result_coms.com_list[0]
    result: Final[LoggerStub] = result_com.result
    get.getLogger_name = result_com.name
    get.result_ut_id = result.ut_id


def Stub_sco_log_get_start(this: Stub_sco_log_get) -> None:

    this.result_src = sco_log.getLogger
    sco_log.getLogger = getLogger_stub


def Stub_sco_log_get_end(this: Stub_sco_log_get) -> None:

    sco_log.getLogger = this.result_src

