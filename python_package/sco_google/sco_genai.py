#!/usr/bin/env python
# coding: UTF-8


import time
import os
from enum import auto
from typing import Final, Optional, Callable, Any
import glob
from google import genai
from google.genai import chats, types

from selenium.webdriver.remote.webdriver import WebDriver
from sco_bas.ScoEnum import ScoEnum
from sco_file.sco_tail import sco_str_tail
from sco_file.sco_truncate import sco_file_truncate
from sco_file.sco_ftext import sco_ftext_append, sco_ftext_read
from sco_log.sco_log import (
    ScoLogger,
    sco_log_get,
    sco_log_last_get
)


GS_GENAI_MODEL   : Final[str] = "gemini-2.0-flash-lite"
GS_INPUT_VERIFY  : Final[str] = "genai"
GS_INPUT_VERIFYUP: Final[str] = GS_INPUT_VERIFY + "up"


class Genai2WayRet(ScoEnum):

    OK       : Final[int] = auto()
    EMPTY    : Final[int] = auto()
    NG_UPLOAD: Final[int] = auto()
    NG_SEND  : Final[int] = auto()
    NG_OUTPUT: Final[int] = auto()


class ScoGenaiUser:

    def __init__(self):
        self.web_drv: Optional[WebDriver] = None


def sco_genai_client() ->\
    tuple[Optional[Exception], Optional[genai.Client]]:

    client    : genai.Client = None
    result_exc: Optional[Exception] = None

    try: client = genai.Client()

    except Exception as exc:
        result_exc = exc

    return (result_exc, client)


def sco_genai_chat_create(client: genai.Client) ->\
    tuple[Optional[Exception], Optional[chats.Chat]]:

    chat      : Optional[chats.Chat] = None
    result_exc: Optional[Exception]  = None

    try: chat = client.chats.create(model = GS_GENAI_MODEL)
    except Exception as exc:
        result_exc = exc

    return (result_exc, chat)


def sco_genai_chatting(client: genai.Client, chat: chats.Chat,
    s_fpath_in: str, s_fpath_md: str, s_fpath_list: str, s_fpath_out: str,
    f_cb: Optional[Callable[[str, Any], None]], user: Optional[ScoGenaiUser])\
    -> None:

    f_cycle_sec : float = 1.0
    f_last_mtime: float = - 1.0
    f_new_mtime : float

    while True:
        send_ret: Genai2WayRet = Genai2WayRet.NG_SEND

        f_new_mtime = input_wait(s_fpath_in, f_cycle_sec, f_last_mtime)
        exc, s_in, i_truncate, as_upname =\
            input_signature(s_fpath_in, s_fpath_md)

        if - 1 < i_truncate:
            exc, send_ret = genai_2way(client, chat, s_in[0: i_truncate],
                                     as_upname, s_fpath_list, s_fpath_out)

        if (send_ret == Genai2WayRet.OK) or (send_ret == Genai2WayRet.EMPTY):
            f_last_mtime = f_new_mtime

        if send_ret == Genai2WayRet.OK:
            exc = sco_file_truncate(s_fpath_in, i_truncate)
            f_cycle_sec = 1.0

            if callable(f_cb):
                f_cb(s_fpath_out, user)

        if exc:
            chatting_exception(exc, s_fpath_out)


def chatting_exception(exc: Exception, s_fpath_out: str) -> None:

    log: Final[ScoLogger] = sco_log_get()

    f_cycle_sec = 60.0
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


def input_signature(s_fpath_in: str, s_fpath_md: str) ->\
    tuple[Optional[Exception], str, int, list[str]]:

    as_upname : list[str] = []
    s_tail    : str = ""
    i_truncate: int = - 1

    exc, s_in = sco_ftext_read(s_fpath_in)

    if not exc:
        i_tail, as_tail = sco_str_tail(s_in, 1)

        if as_tail and (0 < len(as_tail)):
            s_tail = as_tail[- 1].strip()

    if (s_tail == GS_INPUT_VERIFY) or (s_tail == GS_INPUT_VERIFYUP):
        ab_utf8: Final[bytes] = s_in[:i_tail].encode("utf-8")
        i_truncate = len(ab_utf8)

    if s_tail == GS_INPUT_VERIFYUP:
        s_md_name, s_md_ext = os.path.splitext(s_fpath_md)
        as_upname = glob.glob(s_md_name + "[0-9]*" + s_md_ext)

    return (exc, s_in, i_truncate, as_upname)


def genai_2way(client: genai.Client, chat: chats.Chat, s_in: str,
    as_upname: list[str], s_fpath_list: str, s_fpath_out: str)\
    -> tuple[Optional[Exception], Genai2WayRet]:

    exc : Optional[Exception] = None
    ret : Genai2WayRet = Genai2WayRet.EMPTY

    if (0 < len(as_upname)) or (1024 < len(s_in)) or s_in.strip():
        ret = Genai2WayRet.OK

        a_upfile: Final[list[types.File]] = upload_file_async(client, as_upname)
        b_uploaded: Final[bool] = upload_file_wait(a_upfile)

        if b_uploaded:
            exc, res = chat_send_message(client, chat, s_in, a_upfile)

            if exc:
                ret = Genai2WayRet.NG_SEND
        else:
            ret = Genai2WayRet.NG_UPLOAD

        if ret == Genai2WayRet.OK:
            s_time: Final[str] = time.ctime()
            s_out : Final[str] = (
                f"\n--- Update: {s_time} ---  \n"
                f"{res.text if res else 'No response content.'}\n"
            )
            exc, _ = sco_ftext_append(s_fpath_out, s_out)

            if not exc:
                upload_file_remove(as_upname, s_fpath_list)
            else:
                ret = Genai2WayRet.NG_OUTPUT

    return (exc, ret)


def upload_file_async(client: genai.Client, as_upname: list[str]) ->\
    list[types.File]:

    a_upfile: Final[list[types.File]] = []

    print("upload_file_async start")

    for s_upname in as_upname:
        upfile: Final[types.File] = client.files.upload(file = s_upname)
        a_upfile.append(upfile)

    print("upload_file_async finish")
    return a_upfile


def upload_file_wait(a_upfile: list[types.File]) -> bool:

    b_uploaded: bool = True;

    for i_idx in range(len(a_upfile)):
        while a_upfile[i_idx].state.name == "PROCESSING":
            time.sleep(1.0)
            a_upfile[i_idx] = genai.get_file(a_upfile[i_idx].name)
            print("upload processing")

        b_uploaded = (a_upfile[i_idx].state.name == "ACTIVE")

        if not b_uploaded:
            break

    print("upload active %d" % b_uploaded)
    return b_uploaded


def upload_file_remove(as_upname: list[str], s_fpath_list: str) -> None:

    for s_upname in as_upname:
        os.remove(s_upname)

    if 0 < len(as_upname):
        exc = sco_file_truncate(s_fpath_list, 0)


def chat_send_message(client: genai.Client, chat: chats.Chat, s_in: str,
    a_upfile: list[types.File])\
    -> tuple[Optional[Exception], Optional[types.GenerateContentResponse]]:

    res       : types.GenerateContentResponse = None
    result_exc: Optional[Exception] = None

    try:
        config: Final[types.GenerateContentConfig] =\
            types.GenerateContentConfig(http_options = {'timeout': 120 * 1000})

        res = chat.send_message(message = [s_in, *a_upfile], config = config)
    except Exception as exc:
        result_exc = exc

    finally:
        for upfile in a_upfile:
            client.files.delete(name = upfile.name)

    return (result_exc, res)


