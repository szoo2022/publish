#!/usr/bin/python3
# coding: UTF-8


# sys.py
from sys import \
    exit

# logging.py
from logging import \
    Logger

# typing.py
from typing import \
    Final

# sco_def.py
from sco_bas.sco_def import \
    SCO_MODULE_NAME_MAIN

# ScoRc.py
from sco_bas.ScoRc import \
    ScoRc

# sco_ut.py
from sco_ods.sco_ut import \
    SCO_UT_AN_ITEM_T, \
    sco_ut_run

# sco_log.py
from sco_log.sco_log import \
    sco_log_init, \
    sco_log_get

# ut_sco_log_get.py
from ut_sco_log_get.ut_sco_log_get import \
    ut_sco_log_get

# ut_sco_log_init.py
from ut_sco_log_init.ut_sco_log_init import \
    ut_sco_log_init


UT_SCO_LOG_ODS: Final[str] = "ut_sco_log.ods"


def ut_sco_log_main() -> int:

    sheetfnc: Final[dict[str, SCO_UT_AN_ITEM_T]] = \
    { \
        "sco_log_get": ut_sco_log_get, \
        "sco_log_init": ut_sco_log_init, \
    }
    ret: ScoRc
    result: int = 0

    sco_log_init()
    log: Final[Logger] = sco_log_get()

    ret = sco_ut_run(UT_SCO_LOG_ODS, sheetfnc)

    if (ret != ScoRc.OK):
        result = 1
        log.warning("sco_ut_run() failed.")

    return result


if (__name__ == SCO_MODULE_NAME_MAIN):
    exit(ut_sco_log_main())


