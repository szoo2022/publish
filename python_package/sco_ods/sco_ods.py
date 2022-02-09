#!/usr/bin/python3
# coding: UTF-8


from typing         import Final, Optional  # typing.py
from logging        import Logger           # logging.py
from ezodf.document import PackagedDocument # ezodf.py
from ezodf          import opendoc          # ezodf.py
from ezodf.cells    import Cell             # ezodf.py

# ScoRc.py
from sco_bas.ScoRc import \
    ScoRc

# ScoEzodfCellSpan.py
from sco_bas.ScoEzodfCellSpan import \
    ScoEzodfCellSpan

# ScoOdsRng.py
from .ScoOdsRng import \
    ScoOdsRng, \
    ScoOdsRng_create

# sco_log.py
from sco_log.sco_log import \
    sco_log_get


def sco_ods_open(fname: str) -> Optional[PackagedDocument]:

    log   : Final[Logger] = sco_log_get();
    result: PackagedDocument

    try:
        result = opendoc(fname)
    except KeyError as exc:
        result = None
        log.error(f"{exc.__class__.__name__}({fname})")

    return result


def sco_ods_save(ods: PackagedDocument) -> ScoRc:

    log   : Final[Logger] = sco_log_get();
    result: ScoRc = ScoRc.OK

    try:
        ods.save()

    except PermissionError as exc:
        result = ScoRc.NG
        log.error(f"{exc.__class__.__name__} in save.")

    return result


def sco_ods_get_col_rng(mat: list[list[Cell]], col_name: str) \
    -> tuple[int, ScoOdsRng]:

    result_row: int = - 1
    result_rng: Final[ScoOdsRng] = ScoOdsRng_create(- 1, 0)
    text: str = ""

    for row in range(len(mat)):
        for col in range(len(mat[row])):
            cell: Cell = mat[row][col]
            text = cell.plaintext()

            if (text == col_name):
                result_row = row
                result_rng.start  = col
                result_rng.length = cell.span[ScoEzodfCellSpan.COL.zbi]
                break

        if (text == col_name):
            break

    return (result_row, result_rng)

