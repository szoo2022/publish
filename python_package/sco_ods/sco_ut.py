#!/usr/bin/python3
# coding: UTF-8


# typing.py
from typing import \
    Callable, \
    Final, \
    Optional, \
    Any

# logging.py
from logging import \
    Logger

# document.py
from ezodf.document import \
    PackagedDocument

# table.py
from ezodf.table import \
    Table

# cells.py
from ezodf.cells import \
    Cell

# ScoRc.py
from sco_bas.ScoRc import \
    ScoRc

# sco_def.py
from sco_bas.sco_def import \
    Sco_int

# ScoEzodfCellValueType.py
from sco_bas.ScoEzodfCellValueType import \
    ScoEzodfCellValueType

# sco_bltin.py
from sco_bas.sco_bltin import \
    sco_module_eval

# sco_log.py
from sco_log.sco_log import \
    sco_log_get

# ScoUtHead.py
from .ScoUtHead import \
    ScoUtHead

# ScoOdsRng.py
from .ScoOdsRng import \
    ScoOdsRng, \
    ScoOdsRng_create

# ScoUtCols.py
from .ScoUtCols import \
    ScoUtCols, \
    ScoUtCols_set

# sco_ods.py
from .sco_ods import \
    sco_ods_open, \
    sco_ods_save


SCO_UT_AN_ITEM_T = \
    Callable \
    [ \
        [ \
            list[Cell], \
            ScoUtCols   \
        ], \
        tuple[ScoRc, ScoRc] \
    ]


def sco_ut_run(fname: str, sheetfnc: dict[str, SCO_UT_AN_ITEM_T]) -> ScoRc:

    ret   : ScoRc
    result: ScoRc = ScoRc.OK
    log: Final[Logger] = sco_log_get()
    ods: Final[Optional[PackagedDocument]] = sco_ods_open(fname)

    if (ods is not None):
        for sheet in ods.sheets:
            fnc: SCO_UT_AN_ITEM_T = sheetfnc.get(sheet.name)

            if (callable(fnc)):
                ret = sco_ut_run_sheet(sheet, fnc)

                if (ret != ScoRc.OK):
                    log.warning(f"Sheet[{sheet.name}] failed.")
            else:
                log.warning(f"Callback({sheet.name}) is not callable.")

        result = sco_ods_save(ods)

        if (result != ScoRc.OK):
            result = ScoRc.NG
            log.error(f"sco_ods_save({fname}) failed.")
    else:
        result = ScoRc.NG
        log.error(f"sco_ods_open({fname}) failed.")

    return result


def sco_ut_run_sheet(sheet: Table, fnc: SCO_UT_AN_ITEM_T) -> ScoRc:

    ut_cols: ScoUtCols = ScoUtCols()
    result : ScoRc = ScoRc.OK
    log: Final[Logger] = sco_log_get()

    mat: Final[list[list[Cell]]] = [row for row in sheet.rows()]
    ScoUtCols_set(ut_cols, mat)
    rng_number: Final[ScoOdsRng] = ut_cols.cols[ScoUtHead.NUMBER.zbi]
    row_rng: Final[ScoOdsRng] = \
        sco_ut_get_row_rng(mat, ut_cols.row_number, rng_number)

    if ((0 <= row_rng.start) and (0 < row_rng.length)):
        print(f"--- {sheet.name}")
        result = sco_ut_run_matrix(
            mat[row_rng.start: row_rng.start + row_rng.length], ut_cols, fnc)

        if (result != ScoRc.OK):
            result = ScoRc.NG
            log.error("sco_ut_run_matrix() failed.")
    else:
        result = ScoRc.NG
        log.error("sco_ut_get_row_rng() failed.")

    return result


def sco_ut_get_row_rng(mat: list[list[Cell]], row_start: int, \
    col_rng: ScoOdsRng) -> ScoOdsRng:

    result: Final[ScoOdsRng] = ScoOdsRng_create(- 1, 0)
    log   : Final[Logger] = sco_log_get()

    if ((0 <= row_start) and (0 <= col_rng.start) and (0 < col_rng.length)):
        need_len: Final[int] = col_rng.start + col_rng.length

        for row in range(row_start + 1, len(mat) + 1):
            is_num: bool = False

            if (row < len(mat)):
                if (need_len <= len(mat[row])):
                    is_num = (mat[row][need_len - 1].value_type \
                        == ScoEzodfCellValueType.NUMERIC.value)

            if (result.start < 0):
                if (is_num):
                    result.start = row
            else:
                if (not is_num):
                    result.length = row - result.start
                    break
    else:
        log.error("Parameter error.")

    return result


def sco_ut_run_matrix(mat: list[list[Cell]], ut_cols: ScoUtCols, \
    fnc: SCO_UT_AN_ITEM_T) -> ScoRc:

    cnt_test: int = 0
    cnt_ok  : int = 0
    cnt_ng  : int = 0
    cnt_fail: int = 0
    ret     : ScoRc
    judge   : ScoRc
    result  : ScoRc = ScoRc.OK
    log: Final[Logger] = sco_log_get()

    if (callable(fnc)):
        for row in mat:
            (ret, judge) = fnc(row, ut_cols)
            cnt_test += 1

            if (ret == ScoRc.OK):
                if (judge == ScoRc.OK):
                    cnt_ok += 1
                else:
                    cnt_ng += 1
            else:
                cnt_fail += 1

        print(f"All:{cnt_test: 3}, OK:{cnt_ok: 3}, NG:{cnt_ng: 3}, " \
            f"Fail:{cnt_fail: 3}")
    else:
        result = ScoRc.NG
        log.error("fnc is not callable.")

    return result


def sco_ut_cell_get_int(this: Cell, io_res: Optional[Sco_int]) -> int:

    res: int = ScoRc.OK.zbi
    result: int = 0
    log: Final[Logger] = sco_log_get()

    if (this.value_type == ScoEzodfCellValueType.NUMERIC.value):
        result = int(this.value)
    else:
        res = ScoRc.NG.zbi
        log.error("this.value_type is not numeric.")

    if (io_res is not None):
        io_res.value |= res

    return result


def sco_ut_cell_get_eval(this: Cell, io_res: Optional[Sco_int], frm: str) \
    -> Any:

    ret: ScoRc
    imp: Final[str] = this.plaintext()

    (ret, result) = sco_module_eval(frm, imp)

    if ((io_res is not None) and (ret != ScoRc.OK)):
        io_res.value |= ScoRc.NG.zbi

    return result


def sco_ut_get_cells(cell_list: list[Cell], ut_cols: ScoUtCols, \
    head: ScoUtHead) -> list[Cell]:

    result: list[Cell] = []
    col_rng: Final[ScoOdsRng] = ut_cols.cols[head.zbi]
    col_rng_end: Final[int] = col_rng.start + col_rng.length

    if ((0 <= col_rng.start) and (0 < col_rng.length) and \
        (col_rng_end <= len(cell_list)) \
    ):
        result = cell_list[col_rng.start: col_rng_end]

    return result

