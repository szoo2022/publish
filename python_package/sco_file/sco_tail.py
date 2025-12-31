#!/usr/bin/env python
# coding: UTF-8

from typing import Final, Optional, BinaryIO
import os
import mmap
from sco_log.sco_log import (
    ScoLogger,
    sco_log_get
)


def sco_file_tail(s_fpath: str, i_nline: int, s_enc: str = "utf-8")\
    -> Optional[list[str]]:

    as_line: Optional[list[str]] = None
    log    : Final[ScoLogger] = sco_log_get()

    try:
        with open(s_fpath, "rb") as fio:
            fno: Final[int] = fio.fileno();

            with mmap.mmap(fno, 0, access = mmap.ACCESS_READ) as mio:
                ab_line: Final[list[bytes]] = sco_mmap_tail(mio, i_nline)
                as_line = [b_line.decode(s_enc) for b_line in ab_line]

    except (OSError, ValueError, UnicodeDecodeError) as exc:
        log.error(f"{exc}")

    return as_line


def sco_mmap_tail(mio: mmap, i_nline: int) -> list[bytes]:

    ab_line : Final[list[bytes]] = []
    i_size  : Final[int] = mio.size()
    i_pos   : int = i_size

    while (- 1 < i_pos) and (len(ab_line) < i_nline):
        i_new_pos: Final[int] = mio.rfind(b"\n", 0, i_pos)

        if - 1 < i_new_pos:
            if i_new_pos < (i_size - 1): # If a newline is found and it's not
                                         # the very last byte of the file.
                ab_line.insert(0, mio[i_new_pos + 1: i_pos + 1])
        else:
            ab_line.insert(0, mio[0: i_pos + 1])

        i_pos = i_new_pos

    return ab_line


def sco_str_tail(s_in: str, i_nline: int) -> list[bytes]:

    ab_line: Final[list[str]] = []
    i_size : Final[int] = len(s_in)
    i_pos  : int = i_size

    while (- 1 < i_pos) and (len(ab_line) < i_nline):
        i_new_pos: Final[int] = s_in.rfind("\n", 0, i_pos)

        if - 1 < i_new_pos:
            if i_new_pos < (i_size - 1): # If a newline is found and it's not
                                         # the very last byte of the file.
                ab_line.insert(0, s_in[i_new_pos + 1: i_pos + 1])
        else:
            ab_line.insert(0, s_in[0: i_pos + 1])

        i_pos = i_new_pos

    return ab_line


# slow version
def sco_file_tail_read(s_fpath: str, i_nline: int, s_enc: str = "utf-8")\
    -> Optional[list[str]]:

    as_line: Optional[list[str]] = None
    log    : Final[ScoLogger] = sco_log_get()

    try:
        with open(s_fpath, "rb") as fio:
            fio.seek(0, os.SEEK_END)
            i_seek_end : Final[int] = fio.tell()
            i_seek_tail: Final[int] = i_seek_end - 1 # Point to the last character.

            ab_line: Final[list[bytes]] = file_tail_read_extract(
                                            fio, i_seek_tail, i_nline)
            as_line = [b_line.decode(s_enc) for b_line in ab_line]

    except (OSError, UnicodeDecodeError) as exc:
        log.error(f"{exc}")

    return as_line


# slow version
# private
def file_tail_read_extract(fio: BinaryIO, i_seek_tail: int, i_nline: int)\
    -> list[bytes]:

    b_line    : bytes = b""
    i_lf      : int = 0
    ab_line   : Final[list[bytes]] = []
    i_seek_cur: int

    for i_seek_cur in range(i_seek_tail, - 1, - 1):

        fio.seek(i_seek_cur)
        char = fio.read(1)

        if (char == b"\n") and (i_seek_cur < i_seek_tail):
            ab_line.append(b_line)
            b_line = b""
            i_lf += 1

        if (i_lf < i_nline):
            b_line = char + b_line
        else:
            break

    if b_line:
        ab_line.append(b_line)

    ab_line.reverse()
    return ab_line


