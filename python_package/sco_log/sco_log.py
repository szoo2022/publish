#!/usr/bin/env python
# coding: UTF-8


from typing import Final, Optional

from logging import (
    Logger,
    Formatter,
    StreamHandler,
    FileHandler,
    Handler,
    DEBUG,
    getLogger,
    setLoggerClass,
)

from contextlib import contextmanager


LOG_NAME  : Final[str] = "sco_log"
LOG_LEVEL : Final[int] = DEBUG
LOG_FORMAT: Final[str] = (
    "%(asctime)s - %(levelname)8s - %(pathname)s(%(lineno)4d) - "
    "%(funcName)s()\n"
    "%(message)s"
)


class ScoMemoryHandler(Handler):

    def __init__(self):
        super().__init__()
        self.s_last = ""

    def emit(self, record):
        self.s_last = self.format(record)


class ScoLogger(Logger):

    def __init__(self, name, level=0):

        super().__init__(name, level)
        self.h_memory: Optional[ScoMemoryHandler] = None


def sco_log_init() -> None:

    setLoggerClass(ScoLogger)

    log     : Final[ScoLogger] = sco_log_get()
    form    : Final[Formatter] = Formatter(LOG_FORMAT)
    h_stream: Final[StreamHandler] = StreamHandler()
    h_memory: Final[ScoMemoryHandler] = ScoMemoryHandler()

    h_stream.setLevel(LOG_LEVEL)
    h_stream.setFormatter(form)

    h_memory.setLevel(LOG_LEVEL)
    h_memory.setFormatter(form)

    log.setLevel(LOG_LEVEL)
    log.addHandler(h_stream)
    log.addHandler(h_memory)
    log.h_memory = h_memory


def sco_log_get() -> ScoLogger:

    log: Final[ScoLogger] = getLogger(LOG_NAME)

    return log


def sco_log_last_get() -> str:

    log: Final[ScoLogger] = getLogger(LOG_NAME)

    return log.h_memory.s_last


@contextmanager
def sco_log_tee(log: Logger, s_fpath: str):

    h_file: Final[FileHandler] = FileHandler(s_fpath,
                                 mode='a', encoding='utf-8')
    form: Final[Formatter] = Formatter(LOG_FORMAT)
    h_file.setFormatter(form)
    log.addHandler(h_file)

    try:
        yield # Execute with block
    finally:
        log.removeHandler(h_file)
        h_file.close()

