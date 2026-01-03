#!/usr/bin/env python
# coding: UTF-8


import os
import re
from typing import Optional


def sco_ftext_replace_multiline(s_fpath: str, s_regex: str, s_new: str)\
    -> tuple[Optional[Exception], int]:

    i_cnt : int = 0
    result_exc: Optional[Exception] = None
    s_ftmp: Final[str] = s_fpath + '.tmp'

    try:
        with open(s_fpath, 'r', encoding='utf-8') as f_i, \
             open(s_ftmp , 'w', encoding='utf-8') as f_o:

            for s_line in f_i:
                s_rep: Final[str] = re.sub(s_regex, s_new, s_line)
                f_o.write(s_rep)

                if s_rep != s_line:
                    i_cnt += 1

        os.replace(s_ftmp, s_fpath)

    except Exception as exc:
        result_exc = exc
        if os.path.exists(s_ftmp):
            os.remove(s_ftmp)

    return (result_exc, i_cnt)


def sco_ftext_append(s_fpath: str, s_write: str)\
    -> tuple[Optional[Exception], int]:

    result_exc: Optional[Exception] = None
    i_wrote   : int = - 1

    try:
        with open(s_fpath, "a", encoding="utf-8") as fio:
            i_wrote = fio.write(s_write)

    except Exception as exc:
        result_exc = exc

    return (result_exc, i_wrote)


def sco_ftext_read(s_fpath: str) -> tuple[Optional[Exception], Optional[str]]:

    result_exc: Optional[Exception] = None
    s_read    : Optional[str] = None

    try:
        with open(s_fpath, "r", encoding = "utf-8") as fio:
            s_read = fio.read()

    except Exception as exc:
        result_exc = exc

    return (result_exc, s_read)


def sco_ftext_overwrite(s_fpath: str, s_write: str) ->\
    tuple[Optional[Exception], int]:

    result_exc: Optional[Exception] = None
    i_wrote   : int = - 1

    try:
        with open(s_fpath, "w", encoding = "utf-8") as fio:
            i_wrote = fio.write(s_write)

    except Exception as exc:
        result_exc = exc

    return (result_exc, i_wrote)

