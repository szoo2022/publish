#!/usr/bin/env python
# coding: UTF-8


from typing import Optional, Final
from selenium.webdriver.remote.webdriver import WebDriver


def sco_browser_tab_search(web_drv: WebDriver, s_url: str) -> list[str]:

    as_handle: list[str] = []

    for s_handle in web_drv.window_handles:
        if web_drv.current_url == s_url:
            as_handle.append(s_handle)

    return as_handle


def sco_browser_tab_update(web_drv: WebDriver, as_handle: list[str]) -> None:

    for s_handle in as_handle:
        sco_browser_switch_to_window(web_drv, s_handle)
        web_drv.refresh()


def sco_browser_switch_to_window(web_drv: WebDriver, s_handle: str) ->\
    Optional[Exception]:

    ret_exc: Optional[Exception] = None

    try: web_drv.switch_to.window(s_handle)
    except Exception as exc:
        ret_exc = exc

    return ret_exc


