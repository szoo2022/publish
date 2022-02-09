#!/usr/bin/python3
# coding: UTF-8


# typing.py
from typing import \
    Final

# copy.py
from copy import \
    copy

# logging.py
from logging import \
    Logger

# ezodf.py
from ezodf.cells import \
    Cell

# ScoUtHead.py
from .ScoUtHead import \
    ScoUtHead

# ScoOdsRng.py
from .ScoOdsRng import \
    ScoOdsRng, \
    ScoOdsRng_create

# sco_ods.py
from .sco_ods import \
    sco_ods_get_col_rng


class ScoUtCols:

    def __init__(self) -> None:

        self.row_number: int = - 1
        self.cols: Final[list[ScoOdsRng]] = []

        for enm in ScoUtHead:
            rng: ScoOdsRng = ScoOdsRng_create(- 1, 0)
            self.cols.append(rng)


def ScoUtCols_init(this: ScoUtCols) -> None:

    this.row_number = - 1

    for rng in this.cols:
        rng.start = - 1
        rng.length = 0


def ScoUtCols_set(this: ScoUtCols, mat: list[list[Cell]]) -> None:

    row    : int
    col_rng: ScoOdsRng

    ScoUtCols_init(this)

    for enm in ScoUtHead:
        (row, col_rng) = sco_ods_get_col_rng(mat, enm.value)

        if ((0 <= row) and (- 1 < col_rng.start) and (0 < col_rng.length)):
            this.cols[enm.zbi] = copy(col_rng)

            if (enm == ScoUtHead.NUMBER):
                this.row_number = row


