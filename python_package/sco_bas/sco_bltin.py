#!/usr/bin/python3
# coding: UTF-8


# typing.py
from typing import \
    Final, \
    Any

# types.py
from types import \
    ModuleType

# logging.py
from logging import \
    Logger

from importlib import \
    import_module

from varname import \
    nameof

# ScoRc.py
from .ScoRc import \
    ScoRc

# sco_def.py
from .sco_def  import \
    SCO_CB_ANY_T

# sco_log.py
from sco_log.sco_log import \
    sco_log_get


def sco_module_eval(frm: str, imp: str) -> tuple[ScoRc, Any]:

    result: ScoRc = ScoRc.OK
    stuff: Any = None
    mod: ModuleType
    log: Final[Logger] = sco_log_get

    try:
        mod = import_module(frm)
        exp: Final[str] = nameof(mod) + "." + imp
        stuff = eval(exp)

    except (ModuleNotFoundError, NameError, SyntaxError) as exc:
        result = ScoRc.NG
        log.error(f"{exc.__class__.__name__} {frm}")

    return (result, stuff)


def sco_try_cb_any(cbf: SCO_CB_ANY_T, cbf_arg: Any, excs: tuple) \
    -> tuple[ScoRc, Any]:

    result    : ScoRc  = ScoRc.SUCCESS
    result_any: Any    = None
    log: Final[Logger] = sco_log_get()

    for exc in excs:
        if (not BaseException in exc.__mro__[1:]):
            result = ScoRc.FAILURE
            log.error("Exception type must be derived from BaseException.")
            break

    if (result == ScoRc.SUCCESS):
        if (callable(cbf)):
            if (0 < len(excs)):
                try:
                    result_any = cbf(cbf_arg)

                except excs as exc:
                    result = ScoRc.FAILURE
                    log.error(f"{exc.__class__.__name__} in cbf()")
            else:
                result_any = cbf(cbf_arg)
        else:
            result = ScoRc.FAILURE
            log.error("cbf is not callable.")

    return (result, result_any)

