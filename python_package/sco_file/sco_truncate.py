#!/usr/bin/env python
# coding: UTF-8


from typing import Optional
import os


def sco_file_truncate(s_fpath: str, i_size: int) -> Optional[Exception]:

    result_exc: Optional[Exception] = None

    try: os.truncate(s_fpath, i_size)
    except Exception as exc:
        result_exc = exc

    return result_exc


