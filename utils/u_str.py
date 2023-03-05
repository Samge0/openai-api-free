#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/3/6 03:18
# @Author  : Samge


def sub(v: str, length: int, show_ellipsis: bool = True) -> str:
    """
    截断字符串
    :param v:字符串
    :param length: 需要截断的长度
    :param show_ellipsis: 截断后是否显示省略号，默认true
    :return:
    """
    v = v or ''
    curr_size: int = len(v)
    if curr_size > length:
        return f"{v[:length]}……" if show_ellipsis else v[:length]
    else:
        return v
