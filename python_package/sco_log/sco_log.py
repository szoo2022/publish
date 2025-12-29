#!/usr/bin/python3
# coding: UTF-8


from typing import Final

from logging import (
    Logger,
    Formatter,
    StreamHandler,
    FileHandler,
    DEBUG,
    getLogger
)

from contextlib import contextmanager


LOG_NAME  : Final[str] = "sco_log"
LOG_LEVEL : Final[int] = DEBUG
LOG_FORMAT: Final[str] = (
    "%(asctime)s - %(levelname)8s - %(pathname)s(%(lineno)4d) - "
    "%(funcName)s()\n"
    "%(message)s"
)


def sco_log_init() -> None:

    fmt: Final[Formatter] = Formatter(LOG_FORMAT)

    sth: Final[StreamHandler] = StreamHandler()
    sth.setLevel(LOG_LEVEL)
    sth.setFormatter(fmt)

    log: Final[Logger] = sco_log_get()
    log.setLevel(LOG_LEVEL)
    log.addHandler(sth)


def sco_log_get() -> Logger:

    result: Final[Logger] = getLogger(LOG_NAME)

    return result


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

