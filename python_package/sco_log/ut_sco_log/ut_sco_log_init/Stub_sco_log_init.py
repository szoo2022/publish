#!/usr/bin/python3
# coding: UTF-8


# typing.py
from typing import \
    Final, \
    Callable

# sco_log.py
from sco_log import \
    sco_log

# Spec_sco_log_init.py
from .Spec_sco_log_init import \
    Input_sco_log_init, \
    Expect_sco_log_init

# ScoStubComs.py
from sco_stub.ScoStubComs import \
    ScoStubComs_init

# Formatter.py
from sco_stub.logging.Formatter import \
    StubComs_Formatter, \
    Formatter_stub, \
    FormatterStub, \
    g_StubComs_Formatter_get

# StreamHandler.py
from sco_stub.logging.StreamHandler import \
    StubComs_StreamHandler, \
    StreamHandlerStub_setLevel, \
    StreamHandlerStub_setFormatter, \
    StreamHandlerStub, \
    StreamHandler_stub, \
    g_StubComs_StreamHandler_get

# Logger.py
from sco_stub.logging.Logger import \
    LoggerStub_setLevel, \
    LoggerStub_addHandler, \
    LoggerStub

# sco_log_get.py
from sco_stub.sco_log.sco_log_get import \
    StubComs_sco_log_get, \
    StubCom_sco_log_get, \
    sco_log_get_stub, \
    g_StubComs_sco_log_get_get


class Stub_sco_log_init:

    def __init__(self) -> None:

        self.fmt_coms: Final[StubComs_Formatter] = g_StubComs_Formatter_get()
        self.fmt_src: Callable
        self.sth_coms: Final[StubComs_StreamHandler] = \
            g_StubComs_StreamHandler_get()
        self.sth_src: Callable
        self.log_coms: Final[StubComs_sco_log_get] = \
            g_StubComs_sco_log_get_get()
        self.log_src: Callable


def Stub_sco_log_init_set(this: Stub_sco_log_init, set: Input_sco_log_init) \
    -> None:

    fmt: Final[FormatterStub] = FormatterStub()
    fmt.ut_id = set.Formatter_Formatter_ut_id 
    ScoStubComs_init(this.fmt_coms)
    this.fmt_coms.com_list.append(fmt)

    sth: Final[StreamHandlerStub] = StreamHandlerStub()
    sth.ut_id = set.StreamHandler_StreamHandler_ut_id
    ScoStubComs_init(this.sth_coms) 
    this.sth_coms.com_list.append(sth)
    Stub_sco_log_init_set_sth(sth)

    log_com: Final[StubCom_sco_log_get] = StubCom_sco_log_get()
    log: Final[LoggerStub] = log_com.result
    log.ut_id = set.sco_log_get_Logger_ut_id
    ScoStubComs_init(this.log_coms)
    this.log_coms.com_list.append(log_com)
    Stub_sco_log_init_set_log(log)


def Stub_sco_log_init_set_sth(sth: StreamHandlerStub) -> None:

    setLevel: Final[StreamHandlerStub_setLevel] = \
        StreamHandlerStub_setLevel()
    sth.setLevel_list.append(setLevel)

    setFormatter: Final[StreamHandlerStub_setFormatter] = \
        StreamHandlerStub_setFormatter()
    sth.setFormatter_list.append(setFormatter)


def Stub_sco_log_init_set_log(log: LoggerStub) -> None:

    setLevel: Final[LoggerStub_setLevel] = LoggerStub_setLevel()
    log.setLevel_list.append(setLevel)

    addHandler: Final[LoggerStub_addHandler] = LoggerStub_addHandler()
    log.addHandler_list.append(addHandler)


def Stub_sco_log_init_get(this: Stub_sco_log_init, get: Expect_sco_log_init) \
    -> None:

    fmt: Final[FormatterStub] = this.fmt_coms.com_list[0]
    get.Formatter_fmt = fmt.fmt

    sth: Final[StreamHandlerStub] = this.sth_coms.com_list[0]
    Stub_sco_log_init_get_sth(sth, get)

    log_com: Final[StubCom_sco_log_get] = this.log_coms.com_list[0]
    log: Final[LoggerStub] = log_com.result
    Stub_sco_log_init_get_log(log, get)


def Stub_sco_log_init_get_sth \
    (sth: StreamHandlerStub, get: Expect_sco_log_init) -> None:

    setLevel: Final[StreamHandlerStub_setLevel] = sth.setLevel_list[0]
    get.StreamHandler_setLevel_level = setLevel.level

    setFormatter: Final[StreamHandlerStub_setFormatter] = \
        sth.setFormatter_list[0]
    get.StreamHandler_setFormatter_fmt_ut_id = setFormatter.fmt.ut_id


def Stub_sco_log_init_get_log(log: LoggerStub, get: Expect_sco_log_init) \
    -> None:

    setLevel: Final[LoggerStub_setLevel] = log.setLevel_list[0]
    get.Logger_setLevel_level = setLevel.level

    addHandler: Final[LoggerStub_addHandler] = log.addHandler_list[0]
    get.Logger_addHandler_hdlr_ut_id = addHandler.hdlr.ut_id


def Stub_sco_log_init_start(this: Stub_sco_log_init) -> None:

    this.fmt_src = sco_log.Formatter
    sco_log.Formatter = Formatter_stub

    this.sth_src = sco_log.StreamHandler
    sco_log.StreamHandler = StreamHandler_stub

    this.log_src = sco_log.sco_log_get
    sco_log.sco_log_get = sco_log_get_stub


def Stub_sco_log_init_end(this: Stub_sco_log_init) -> None:

    sco_log.Formatter = this.fmt_src
    sco_log.StreamHandler = this.sth_src
    sco_log.sco_log_get = this.log_src

