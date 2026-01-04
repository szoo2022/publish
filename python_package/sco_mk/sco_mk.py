#!/usr/bin/env python
# coding: UTF-8


import os
from typing import Final

from sco_log.sco_log import ScoLogger, sco_log_get
from sco_file.sco_ftext import sco_ftext_replace_multiline


def makefile_variable_set(s_mk: str, s_var: str, s_val: str) -> None:

    log: Final[ScoLogger] = sco_log_get()

    if os.path.exists(s_mk):
        s_regex: Final[str] = fr'^(\s*{s_var}\s*:?=\s*).*'
        s_new  : Final[str] = fr'\1{s_val}'
        exc, i_repcnt = sco_ftext_replace_multiline(s_mk, s_regex, s_new)

        if exc or (i_repcnt < 1):
            reason = f"exception: {exc}" if exc else "pattern not found"
            log.error(f"Fail to replace '{s_mk_var}' in {s_mk}."
                      f" Reason: {reason}")


