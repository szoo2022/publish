#!/usr/bin/env python
# coding: UTF-8


import os
import re
import shutil
import stat
from typing import Optional

from .sco_truncate import (
    sco_file_truncate
)


def sco_ftext_replace_multiline(s_fpath: str, s_regex: str, s_new: str)\
    -> tuple[Optional[Exception], int]:

    i_cnt : int = 0
    result_exc: Optional[Exception] = None
    s_ftmp: Final[str] = s_fpath + '.tmp'

    try:
        original_mode: Final[int] = os.stat(s_fpath).st_mode

        with open(s_fpath, 'r', encoding='utf-8') as f_i, \
             open(s_ftmp , 'w', encoding='utf-8') as f_o:

            for s_line in f_i:
                s_rep: Final[str] = re.sub(s_regex, s_new, s_line)
                f_o.write(s_rep)

                if s_rep != s_line:
                    i_cnt += 1

        os.chmod(s_ftmp, stat.S_IMODE(original_mode))
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
        with open(s_fpath, "a", encoding="utf-8") as f_o:
            i_wrote = f_o.write(s_write)

    except Exception as exc:
        result_exc = exc

    return (result_exc, i_wrote)


def sco_ftext_read(s_fpath: str) -> tuple[Optional[Exception], Optional[str]]:

    result_exc: Optional[Exception] = None
    s_read    : Optional[str] = None

    try:
        with open(s_fpath, "r", encoding = "utf-8") as f_i:
            s_read = f_i.read()

    except Exception as exc:
        result_exc = exc

    return (result_exc, s_read)


def sco_ftext_reads(s_fpath: str) ->\
    tuple[Optional[Exception], Optional[list[str]]]:

    result_exc: Optional[Exception] = None
    as_read   : Optional[list[str]] = None

    try:
        with open(s_fpath, "r", encoding = "utf-8") as f_i:
            as_read = f_i.readlines()

    except Exception as exc:
        result_exc = exc

    return (result_exc, as_read)


def sco_ftext_overwrite(s_fpath: str, s_write: str) ->\
    tuple[Optional[Exception], int]:

    result_exc: Optional[Exception] = None
    i_wrote   : int = - 1

    try:
        with open(s_fpath, "w", encoding = "utf-8") as f_o:
            i_wrote = f_o.write(s_write)

    except Exception as exc:
        result_exc = exc

    return (result_exc, i_wrote)


# Supported for UTF-8, ASCII, SHIFT-JIS
def sco_ftext_rstrip(s_fpath: str) -> tuple[Optional[Exception], int, int]:

    i_space       : Final[int] = b' '[0]
    i_seek_cur    : int = - 1
    i_seek_end    : int = - 1
    i_seek_end_ret: int = - 1
    result_exc: Optional[Exception] = None

    try:
        with open(s_fpath, "rb") as f_i:
            f_i.seek(0, os.SEEK_END)
            i_seek_end = f_i.tell()

            for i_seek_cur in range(i_seek_end - 1, - 1, - 1):
                f_i.seek(i_seek_cur)
                char: bytes = f_i.read(1)

                if (i_space < char[0]):
                    break;
            else:
                i_seek_cur = - 1

        i_seek_end_ret = i_seek_cur + 1
        result_exc = sco_file_truncate(s_fpath, i_seek_end_ret)

    except (OSError, UnicodeDecodeError) as exc:
        result_exc = exc

    return (result_exc, i_seek_end, i_seek_end_ret)


