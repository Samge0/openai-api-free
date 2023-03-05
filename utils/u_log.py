#!/usr/bin/ruby
# -*- coding : utf-8 -*-
# author：samge
# data：2023-02-28 17:24
# describe：
import os.path

from utils import u_file, u_date

# 是否调试模式
IS_DEBUG = False

# log dir
log_dir = 'logs'


def i(msg):
    _print(msg)


def _print(msg):
    if not IS_DEBUG:
        return
    print(msg)


def save_log(msg: str, file_name: str) -> None:
    """
    保存日志
    :param msg:
    :param file_name:
    :return:
    """
    msg = f"[{u_date.get_today_str()}] {msg}\n"
    print(msg)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    file_path = f'{log_dir}/{file_name}'
    u_file.save(msg, file_path, 'a+')
