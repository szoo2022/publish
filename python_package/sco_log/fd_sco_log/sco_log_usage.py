#!/usr/bin/python3
# coding: UTF-8


from sco_log.sco_log import sco_log_init
from sco_log.sco_log import sco_log_get


def sub_function(param):
    log = sco_log_get()

    if (param is not None):
        log.debug(f"sub_function({param})")
    else:
        log.error("Parameter error.")


def main():
    sco_log_init()
    log = sco_log_get()
    
    log.debug("Start main")
    sub_function(1)
    sub_function(None)


main()


