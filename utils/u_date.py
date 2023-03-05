#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/4 下午6:57
# @Author  : Samge
import datetime
import time


def get_time_stamp(value: int = 1000):
    """获取时间戳"""
    return int(time.time() * value)


def get_today_str(f='%Y-%m-%d %H:%M:%S') -> str:
    """
    获取当天年月日字符串
    :param f:
    :return:
    """
    return time.strftime(f, time.localtime(time.time()))


def is_today_right(c_date):
    """判断日期是否在今天之后，不包含今天"""
    try:
        if not c_date:
            return False
        return (datetime.datetime.strptime(c_date[:10], '%Y-%m-%d') - datetime.datetime.now()).days > 0
    except:
        return False


def timestamp2str(timestamp: int, fmt: str = '%Y-%m-%d %H:%M:%S') -> str:
    """时间戳转日期字符串"""
    try:
        time_array = time.localtime(timestamp)
        return time.strftime(fmt, time_array)
    except:
        return '1970-01-01'
