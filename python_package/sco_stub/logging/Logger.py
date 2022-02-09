#!/usr/bin/python3
# coding: UTF-8


# typing.py
from typing import \
    Final, \
    Optional, \
    TypeAlias, \
    Union

# logging.py
from logging import \
    Logger, \
    Handler

# sco_log.py
from sco_log.sco_log import \
    sco_log_get

# ScoStubComs.py
from sco_stub.ScoStubComs import \
    ScoStubComs, \
    ScoStubInit

# StreamHandler.py
from .StreamHandler import \
    StreamHandlerStub


class LoggerStub_setLevel:

    def __init__(self) -> None:

        self.level: Union[int, str] = ScoStubInit.INT


class LoggerStub_addHandler:

    def __init__(self) -> None:

        self.hdlr: StreamHandlerStub = StreamHandlerStub()


class LoggerStub(Logger):

    def __init__(self) -> None:

        self.ut_id: int = 0

        self.setLevel_list: Final[list[LoggerStub_setLevel]] = []
        self.setLevel_used: int = 0

        self.addHandler_list: \
            Final[list[LoggerStub_addHandler]] = []
        self.addHandler_used: int = 0


    def setLevel(self, level: Union[int, str]) -> None:

        if (self.setLevel_used < len(self.setLevel_list)):
            i_o: Final[LoggerStub_setLevel] = \
                self.setLevel_list[self.setLevel_used]
            i_o.level = level
            self.setLevel_used += 1
        else:
            log: Final[Logger] = sco_log_get()
            log.error("self.setLevel_list is short.")


    def addHandler(self, hdlr: Handler) -> None:

        if (self.addHandler_used < len(self.addHandler_list)):
            i_o: Final[LoggerStub_addHandler] = \
                self.addHandler_list[self.addHandler_used]
            i_o.hdlr = hdlr
            self.addHandler_used += 1
        else:
            log: Final[Logger] = sco_log_get()
            log.error("self.addHandler_list is short.")


StubComs_Logger: TypeAlias = ScoStubComs[LoggerStub]


def Logger_stub() -> Logger:

    result: Optional[LoggerStub] = None
    log: Final[Logger] = sco_log_get()
    coms: Final[StubComs_Logger] = g_StubComs_Logger_get()

    if (coms.com_used < len(coms.com_list)):
        result = coms.com_list[coms.com_used]
        coms.com_used += 1
    else:
        log.error("coms.com_list is short.")

    return result


def g_StubComs_Logger_get() -> StubComs_Logger:

    return g_StubComs_Logger


g_StubComs_Logger: Final[StubComs_Logger] = StubComs_Logger()

