#!/usr/bin/env python
# coding: UTF-8


def sco_file_tail(s_fpath: str, i_nline: int, s_enc: str = "utf-8") ->
    Optional[list[str]]:

    as_line: Optional[list[str]] = None
    log    : Final[ScoLogger] = sco_log_get()

    try:
        with open(s_fpath, "rb") as fio:
            fio.seek(0, os.SEEK_END)
            i_seek_end : Final[int] = fio.tell()
            i_seek_tail: Final[int] = i_seek_end - 1 # Point to the last character.

            ab_line: Final[list[bytes]] = file_tail_extract(
                                            fio, i_seek_tail, i_nline)
            as_line = [b_line.decode(s_enc) for b_line in ab_line]

    except (OSError, UnicodeDecodeError) as exc:
        log.error(f"{exc}")

    return as_line


# private
def file_tail_extract(fio: BinaryIO, i_seek_tail: int, i_nline: int) ->
    list[bytes]:

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

