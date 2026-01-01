#!/usr/bin/env python
# coding: UTF-8


from typing import Optional


def sco_ftext_append(s_fpath_out: str, s_out: str)\
    -> tuple[Optional[Exception], int]:

    result_exc: Optional[Exception] = None
    i_wrote: int = - 1

    try:
        with open(s_fpath_out, "a", encoding="utf-8") as fio:
            i_wrote = fio.write(s_out)

    except Exception as exc:
        result_exc = exc

    return (result_exc, i_wrote)


