#!/usr/bin/python3
# coding: UTF-8


# logging.py
from logging import \
    Logger

# typing.py
from typing import \
    Final

# ezodf.py
from ezodf.cells import \
    Cell

# ScoRc.py
from sco_bas.ScoRc import \
    ScoRc

# ScoUtCols.py
from sco_ods.ScoUtCols import \
    ScoUtCols

# sco_log.py
from sco_log.sco_log import \
    sco_log_get

# Spec_sco_log_get.py
from .Spec_sco_log_get import \
    Number_sco_log_get, \
    Input_sco_log_get, \
    Expect_sco_log_get, \
    Output_sco_log_get, \
    Judge_sco_log_get, \
    Number_sco_log_get_set, \
    Input_sco_log_get_set, \
    Expect_sco_log_get_set, \
    Output_sco_log_get_set, \
    Judge_sco_log_get_set, \
    Output_sco_log_get_write, \
    Judge_sco_log_get_write

# Stub_sco_log_get.py
from .Stub_sco_log_get import \
    Stub_sco_log_get, \
    Stub_sco_log_get_set, \
    Stub_sco_log_get_start, \
    Stub_sco_log_get_end, \
    Stub_sco_log_get_get


def ut_sco_log_get(cell_list: list[Cell], ut_cols: ScoUtCols) \
    -> tuple[ScoRc, ScoRc]:

    number: Final[Number_sco_log_get] = Number_sco_log_get()
    input: Final[Input_sco_log_get] = Input_sco_log_get()
    expect: Final[Expect_sco_log_get] = Expect_sco_log_get()
    output_real: Final[Expect_sco_log_get] = Expect_sco_log_get()
    output: Final[Output_sco_log_get] = Output_sco_log_get()
    judge: Final[Judge_sco_log_get] = Judge_sco_log_get()
    stub: Final[Stub_sco_log_get] = Stub_sco_log_get()
    i_ret: int = 0
    result: ScoRc = ScoRc.OK
    result_test: ScoRc = ScoRc.NG
    log: Final[Logger] = sco_log_get()

    i_ret += Number_sco_log_get_set(number, cell_list, ut_cols)
    i_ret += Input_sco_log_get_set(input, cell_list, ut_cols)
    i_ret += Expect_sco_log_get_set(expect, cell_list, ut_cols)
    i_ret += Output_sco_log_get_set(output, cell_list, ut_cols)
    i_ret += Judge_sco_log_get_set(judge, cell_list, ut_cols)

    if (i_ret == 0):
        Stub_sco_log_get_set(stub, input)
        Stub_sco_log_get_start(stub) 
        sco_log_get()
        Stub_sco_log_get_end(stub)
        Stub_sco_log_get_get(stub, output_real)

        Output_sco_log_get_write(output, output_real)
        result_test = Judge_sco_log_get_write(judge, expect, output_real)
    else:
        result = ScoRc.NG
        log.error('Fail to store cell contents.')

    return (result, result_test)

