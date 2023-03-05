#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/3/6 03:04
# @Author  : Samge
import enum


class AccountSwitchingType(enum.Enum):
    """
    账号切换类型：
        正序=asc
        随机=random
    """
    ASC = "asc",  # 正序
    RANDOM = "random",  # 随机
