#!/usr/bin/env python
# coding: UTF-8


import time
import os
from enum import auto
from typing import Final, Optional
from google import genai
from google.genai import chats, types
from sco_bas.ScoEnum import ScoEnum
from sco_file.sco_tail import sco_str_tail
from sco_file.sco_truncate import sco_file_truncate
from sco_file.sco_fio import sco_ftext_append
from sco_log.sco_log import (
    ScoLogger,
    sco_log_get,
    sco_log_last_get
)


GS_GENAI_MODEL : Final[str] = "gemini-2.5-flash"
GS_INPUT_VERIFY: Final[str] = "genai"


class GenaiSendRet(ScoEnum):

    OK       : Final[int] = auto()
    NG_SEND  : Final[int] = auto()
    NG_OUTPUT: Final[int] = auto()


def genai_client() ->\
    tuple[Optional[Exception], Optional[genai.Client]]:

    client    : genai.Client = None
    result_exc: Optional[Exception] = None

    try: client = genai.Client()

    except Exception as exc:
        result_exc = exc

    return (result_exc, client)


def genai_chat_create(client: genai.Client) ->\
    tuple[Optional[Exception], Optional[chats.Chat]]:

    chat      : Optional[chats.Chat] = None
    result_exc: Optional[Exception]  = None

    try: chat = client.chats.create(model = GS_GENAI_MODEL)
    except Exception as exc:
        result_exc = exc

    return (result_exc, chat)


def genai_chatting(chat: chats.Chat, s_fpath_in: str, s_fpath_out: str) -> None:

    f_cycle_sec : float = 1.0
    f_last_mtime: float = - 1.0
    f_new_mtime : float

    while True:
        send_ret: GenaiSendRet = GenaiSendRet.NG_SEND

        f_new_mtime = input_wait(s_fpath_in, f_cycle_sec, f_last_mtime)
        exc, s_in, i_truncate = input_signature(s_fpath_in)

        if (not exc) and (- 1 < i_truncate):
            exc, send_ret = genai_2way(chat, s_in[0: i_truncate], s_fpath_out)

        if not exc:
            f_last_mtime = f_new_mtime
            f_cycle_sec = 1.0
        else:
            f_cycle_sec = 10.0

        if send_ret == GenaiSendRet.OK:
            exc = sco_file_truncate(s_fpath_in, i_truncate)

        if exc:
            log.error(f"{exc}")
            s_last: Final[str] = sco_log_last_get()
            sco_ftext_append(s_fpath_out, s_last)


def input_wait(s_fpath_in: str, f_cycle_sec: float, f_last_mtime: float) ->\
    float:

    f_new_mtime: float

    while True:
        time.sleep(f_cycle_sec)

        if not os.path.exists(s_fpath_in):
            sco_ftext_append(s_fpath_in, "Hello World\n")

        f_new_mtime: Final[float] = os.path.getmtime(s_fpath_in)

        if (f_last_mtime < 0.0):
            f_last_mtime = f_new_mtime

        if (f_last_mtime < f_new_mtime):
            break

    return f_new_mtime


def input_signature(s_fpath: str) -> tuple[Optional[Exception], str, int]:

    i_truncate: int = - 1

    exc, s_in = input_read(s_fpath)

    if not exc:
        i_tail, as_tail = sco_str_tail(s_in, 1)

        if as_tail and (0 < len(as_tail)):
            s_tail: Final[str] = as_tail[- 1].strip()
            if (s_tail == GS_INPUT_VERIFY):
                ab_utf8: Final[bytes] = s_in[:i_tail].encode("utf-8")
                i_truncate = len(ab_utf8)

    return (exc, s_in, i_truncate)


def genai_2way(chat: chats.Chat, s_in: str, s_fpath_out: str) ->\
    tuple[Optional[Exception], GenaiSendRet]:

    exc : Optional[Exception] = None
    ret : GenaiSendRet = GenaiSendRet.OK

    if (1024 < len(s_in)) or s_in.strip():
        exc, res = send_message(chat, s_in)

        if not exc:
            s_time: Final[str] = time.ctime()
            s_out : Final[str] = (
                f"\n--- Update: {s_time} ---\n"
                f"{res.text if res else 'No response content.'}\n"
            )
            exc, _ = sco_ftext_append(s_fpath_out, s_out)

            if exc:
                ret = GenaiSendRet.NG_OUTPUT
        else:
            ret = GenaiSendRet.NG_SEND

    return (exc, ret)


def send_message(chat: chats.Chat, s_in: str) ->\
    tuple[Optional[Exception], Optional[types.GenerateContentResponse]]:

    res       : types.GenerateContentResponse = None
    result_exc: Optional[Exception] = None

    try: res = chat.send_message(s_in)
    except Exception as exc:
        result_exc = exc

    return (result_exc, res)


def input_read(s_fpath_in: str) -> tuple[Optional[Exception], str]:

    s_in      : str = "";
    result_exc: Optional[Exception] = None

    try:
        with open(s_fpath_in, "r", encoding="utf-8") as fio:
            s_in = fio.read()

    except Exception as exc:
        result_exc = exc

    return (result_exc, s_in)


