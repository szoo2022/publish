#!/usr/bin/env python
# coding: UTF-8


import os
import shutil
import pathlib
from pathlib import Path
from typing import Optional, Final

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.common.exceptions import WebDriverException


def sco_firefox_ensure(web_drv) -> WebDriver:
    ret_drv: WebDriver

    try:
        _ = web_drv.current_url
        ret_drv = web_drv
    except (WebDriverException, AttributeError):
        ret_drv = sco_firefox_launch()

    return ret_drv


def sco_firefox_launch() -> WebDriver:

    options = Options()
    options.binary_location = sco_firefox_fpath()
    web_drv: Final[WebDriver] = webdriver.Firefox(options=options)

    return web_drv


def sco_firefox_fpath() -> str:

    s_fpath: str = "/snap/firefox/current/usr/lib/firefox/firefox"

    if not os.path.exists(s_fpath):
        s_which: Optional[str] = shutil.which("firefox")

        if s_which:
            fpath: Final[pathlib.Path] = Path(s_which).resolve()
            s_fpath = str(fpath)
        else:
            s_fpath = ""

    return s_fpath


