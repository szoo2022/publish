#!/usr/bin/python3
# coding: UTF-8


# _io.pyi
from _io import \
    TextIOWrapper

# typing.py
from typing import \
    Final, \
    Optional, \
    TypeAlias, \
    Union

# logging.py
from logging import \
    Logger, \
    StreamHandler, \
    Formatter

# sco_log.py
from sco_log.sco_log import \
    sco_log_get

# ScoStubComs.py
from sco_stub.ScoStubComs import \
    ScoStubComs, \
    ScoStubInit

# Formatter.py
from .Formatter import \
    FormatterStub


class StreamHandlerStub_setLevel:

    def __init__(self) -> None:

        self.level: Union[int, str] = ScoStubInit.INT


class StreamHandlerStub_setFormatter:

    def __init__(self) -> None:

        self.fmt: Formatter = FormatterStub()


class StreamHandlerStub(StreamHandler):

    def __init__(self) -> None:

        self.ut_id: int = 0

        self.setLevel_list: Final[list[StreamHandlerStub_setLevel]] = []
        self.setLevel_used: int = 0

        self.setFormatter_list: \
            Final[list[StreamHandlerStub_setFormatter]] = []
        self.setFormatter_used: int = 0


    def setLevel(self, level: Union[int, str]) -> None:

        if (self.setLevel_used < len(self.setLevel_list)):
            i_o: Final[StreamHandlerStub_setLevel] = \
                self.setLevel_list[self.setLevel_used]
            i_o.level = level
            self.setLevel_used += 1
        else:
            log: Final[Logger] = sco_log_get()
            log.error("self.setLevel_list is short.")


    def setFormatter(self, fmt: Formatter) -> None:

        if (self.setFormatter_used < len(self.setFormatter_list)):
            i_o: Final[StreamHandlerStub_setFormatter] = \
                self.setFormatter_list[self.setFormatter_used]
            i_o.fmt = fmt
            self.setFormatter_used += 1
        else:
            log: Final[Logger] = sco_log_get()
            log.error("self.setFormatter_list is short.")


StubComs_StreamHandler: TypeAlias = ScoStubComs[StreamHandlerStub]


def StreamHandler_stub(stream: TextIOWrapper = None) -> StreamHandler:

    result: Optional[StreamHandlerStub] = None
    log: Final[Logger] = sco_log_get()
    coms: Final[StubComs_StreamHandler] = g_StubComs_StreamHandler_get()

    if (coms.com_used < len(coms.com_list)):
        result = coms.com_list[coms.com_used]
        coms.com_used += 1
    else:
        log.error("coms.com_list is short.")

    return result


def g_StubComs_StreamHandler_get() -> StubComs_StreamHandler:

    return g_StubComs_StreamHandler


g_StubComs_StreamHandler: Final[StubComs_StreamHandler] = \
    StubComs_StreamHandler()

