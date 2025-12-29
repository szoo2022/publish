#!/usr/bin/env python
# coding: UTF-8


from typing          import Final, Any, Optional
from types           import ModuleType
from logging         import Logger
from importlib       import import_module
from varname         import nameof
from .ScoRc          import ScoRc
from .sco_def        import SCO_CB_ANY_T
from sco_log.sco_log import sco_log_get


def sco_module_eval(frm: str, imp: str) -> tuple[ScoRc, Any]:

    result: ScoRc = ScoRc.OK
    stuff: Any = None
    mod: ModuleType
    log: Final[Logger] = sco_log_get()

    try:
        mod = import_module(frm)
        exp: Final[str] = nameof(mod) + "." + imp
        stuff = eval(exp)

    except (ModuleNotFoundError, NameError, SyntaxError) as exc:
        result = ScoRc.NG
        log.error(f"{exc.__class__.__name__} {frm}")

    return (result, stuff)


def sco_try_cb_any(
    f_cb: SCO_CB_ANY_T,
    cb_arg: Any,
    tt_exc: tuple[type[BaseException], ...]
) -> tuple[Optional[BaseException], Any]:

    result_exc: Optional[BaseException] = None
    result_any: Any = None

    for t_exc in tt_exc:
        if not (isinstance(t_exc, type) and issubclass(t_exc, BaseException)):
            result_exc = TypeError(f"Invalid exception type: {t_exc}")
            break

    if (not result_exc) and (not callable(f_cb)):
        result_exc = TypeError("f_cb is not callable.")

    if not result_exc:
        if tt_exc:
            try:
                result_any = f_cb(cb_arg)

            except tt_exc as t_exc:
                result_exc = t_exc
        else:
            result_any = f_cb(cb_arg)

    return (result_exc, result_any)

