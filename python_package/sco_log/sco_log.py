#!/usr/bin/python3
# coding: UTF-8


# typing.py
from typing import \
    Final

# logging.py
from logging import \
    Logger, \
    Formatter, \
    StreamHandler, \
    DEBUG, \
    getLogger


LOG_NAME  : Final[str] = "sco_log"
LOG_LEVEL : Final[int] = DEBUG
LOG_FORMAT: Final[str] = \
    "%(asctime)s - %(levelname)8s - %(pathname)s(%(lineno)4d) - " \
    "%(funcName)s()\n" \
    "%(message)s"


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

