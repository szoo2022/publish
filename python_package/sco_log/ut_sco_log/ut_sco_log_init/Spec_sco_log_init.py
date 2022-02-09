#!/usr/bin/python3
# coding: UTF-8


# typing.py
from typing import \
    Final

# logging.py
from logging import \
    Logger

# cells.py
from ezodf.cells import \
    Cell

# ScoRc.py
from sco_bas.ScoRc import \
    ScoRc

# sco_def.py
from sco_bas.sco_def import \
    Sco_int

# sco_def.py
from sco_log.sco_log import \
    sco_log_get

# ScoUtHead.py
from sco_ods.ScoUtHead import \
    ScoUtHead

# ScoUtCols.py
from sco_ods.ScoUtCols import \
    ScoUtCols

# sco_ut.py
from sco_ods.sco_ut import \
    sco_ut_cell_get_int, \
    sco_ut_cell_get_eval, \
    sco_ut_get_cells


class Number_sco_log_init:

    def __init__(self) -> None:

        self.number: int = 0


def Number_sco_log_init_set(this: Number_sco_log_init, cell_list: list[Cell], \
    ut_cols: ScoUtCols) -> int:

    log: Final[Logger] = sco_log_get()
    result: ScoRc = ScoRc.OK
    io_res: Final[Sco_int] = Sco_int()
    io_res.value = 0

    cells: Final[list[Cell]] = \
        sco_ut_get_cells(cell_list, ut_cols, ScoUtHead.NUMBER)

    if (0 < len(cells)):
        this.number = sco_ut_cell_get_int(cells[0], io_res)

        if (io_res.value != 0):
            result = ScoRc.NG
            log.error("Fail to get cell contents.")
    else:
        result = ScoRc.NG
        log.error("cells is short.")

    return result.zbi


class Input_sco_log_init:

    def __init__(self) -> None:

        self.Formatter_Formatter_ut_id: int = 0
        self.StreamHandler_StreamHandler_ut_id: int = 0
        self.sco_log_get_Logger_ut_id: int = 0


def Input_sco_log_init_set(this: Input_sco_log_init, cell_list: list[Cell], \
    ut_cols: ScoUtCols) -> int:

    log: Final[Logger] = sco_log_get()
    result: ScoRc = ScoRc.OK
    io_res: Final[Sco_int] = Sco_int()
    io_res.value = 0

    cells: Final[list[Cell]] = \
        sco_ut_get_cells(cell_list, ut_cols, ScoUtHead.INPUT)

    if (2 < len(cells)):
        this.Formatter_Formatter_ut_id = sco_ut_cell_get_int(cells[0], io_res)
        this.StreamHandler_StreamHandler_ut_id = \
            sco_ut_cell_get_int(cells[1], io_res)
        this.sco_log_get_Logger_ut_id = sco_ut_cell_get_int(cells[2], io_res)

        if (io_res.value != 0):
            result = ScoRc.NG
            log.error("Fail to get cell contents.")
    else:
        result = ScoRc.NG
        log.error("cells is short.")

    return result.zbi


class Expect_sco_log_init:

    def __init__(self) -> None:

        self.Formatter_fmt: str = ""
        self.StreamHandler_setLevel_level: int = 0
        self.StreamHandler_setFormatter_fmt_ut_id: int = 0
        self.Logger_setLevel_level: int = 0
        self.Logger_addHandler_hdlr_ut_id: int = 0


    def __eq__(self, other: object) -> bool:

        return (self.__dict__ == other.__dict__)


def Expect_sco_log_init_set(this: Expect_sco_log_init, cell_list: list[Cell], \
    ut_cols: ScoUtCols) -> int:

    log: Final[Logger] = sco_log_get()
    result: ScoRc = ScoRc.OK
    io_res: Final[Sco_int] = Sco_int()
    io_res.value = 0
    frm: Final[str] = "sco_log.sco_log"

    cells: Final[list[Cell]] = \
        sco_ut_get_cells(cell_list, ut_cols, ScoUtHead.EXPECT)

    if (4 < len(cells)):
        this.Formatter_fmt = sco_ut_cell_get_eval(cells[0], io_res, frm)
        this.StreamHandler_setLevel_level = \
            sco_ut_cell_get_eval(cells[1], io_res, frm)
        this.StreamHandler_setFormatter_fmt_ut_id = \
            sco_ut_cell_get_int(cells[2], io_res)
        this.Logger_setLevel_level = \
            sco_ut_cell_get_eval(cells[3], io_res, frm)
        this.Logger_addHandler_hdlr_ut_id = \
            sco_ut_cell_get_int(cells[4], io_res)

        if (io_res.value != 0):
            result = ScoRc.NG
            log.error("Fail to get cell contents.")
    else:
        result = ScoRc.NG
        log.error("cells is short.")

    return result.zbi


class Output_sco_log_init:

    def __init__(self) -> None:

        self.Formatter_fmt: Cell
        self.StreamHandler_setLevel_level: Cell
        self.StreamHandler_setFormatter_fmt_ut_id: Cell
        self.Logger_setLevel_level: Cell
        self.Logger_addHandler_hdlr_ut_id: Cell


def Output_sco_log_init_set(this: Output_sco_log_init, cell_list: list[Cell], \
    ut_cols: ScoUtCols) -> int:

    log: Final[Logger] = sco_log_get()
    result: ScoRc = ScoRc.OK

    cells: Final[list[Cell]] = \
        sco_ut_get_cells(cell_list, ut_cols, ScoUtHead.OUTPUT)

    if (4 < len(cells)):
        this.Formatter_fmt = cells[0]
        this.StreamHandler_setLevel_level = cells[1]
        this.StreamHandler_setFormatter_fmt_ut_id = cells[2]
        this.Logger_setLevel_level = cells[3]
        this.Logger_addHandler_hdlr_ut_id = cells[4]
    else:
        result = ScoRc.NG
        log.error("cells is short.")

    return result.zbi


def Output_sco_log_init_write(this: Output_sco_log_init, \
    output_real: Expect_sco_log_init) -> None:

    this.Formatter_fmt.set_value(output_real.Formatter_fmt)
    this.StreamHandler_setLevel_level.set_value \
        (output_real.StreamHandler_setLevel_level)
    this.StreamHandler_setFormatter_fmt_ut_id.set_value \
        (output_real.StreamHandler_setFormatter_fmt_ut_id)
    this.Logger_setLevel_level.set_value(output_real.Logger_setLevel_level)
    this.Logger_addHandler_hdlr_ut_id.set_value \
        (output_real.Logger_addHandler_hdlr_ut_id)


class Judge_sco_log_init:

    def __init__(self) -> None:

        self.judge: Cell


def Judge_sco_log_init_set(this: Judge_sco_log_init, cell_list: list[Cell], \
    ut_cols: ScoUtCols) -> int:

    log: Final[Logger] = sco_log_get()
    result: ScoRc = ScoRc.OK

    cells: Final[list[Cell]] = \
        sco_ut_get_cells(cell_list, ut_cols, ScoUtHead.JUDGE)

    if (0 < len(cells)):
        this.judge = cells[0]
    else:
        result = ScoRc.NG
        log.error("cells is short.")

    return result.zbi


def Judge_sco_log_init_write(this: Judge_sco_log_init, \
    expect: Expect_sco_log_init, output_real: Expect_sco_log_init) -> ScoRc:

    result: ScoRc

    if (expect == output_real):
        result = ScoRc.OK
        this.judge.set_value(result.name)
    else:
        result = ScoRc.NG
        this.judge.set_value(result.name)

    return result

