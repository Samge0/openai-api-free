#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/3/4 23:05
# @Author  : Samge
import random

import requests
from revChatGPT.V1 import Chatbot

from models.m_enum import AccountSwitchingType
from utils import u_file, u_log

"""
https://github.com/acheong08/ChatGPT
代理服务器速率限制：每 10 秒 15 个请求（每个 IP）
OpenAI 速率限制：免费帐户每小时 50 个请求。你可以通过多账户循环来绕过它
Plus 帐户每小时有大约 150 个请求的速率限制
"""


def get_chatbot(account_info: str):
    """
    获取机器人
    :param account_info:
    :return:
    """
    msg = f"获取机器人：{account_info}"
    u_log.save_log(msg, 'get_chatbot.log')
    _splits = account_info.split('|')
    email = _splits[0].strip()
    password = _splits[1].strip()
    _proxy = '' if len(_splits) < 3 else _splits[2].strip()
    config = {
        "email": email,
        "password": password,
    }
    if _proxy:
        config['proxy'] = _proxy
    return Chatbot(config)


def get_account_infos(config: dict) -> list:
    """
    获取账户信息列表
        优先从api接口地址中读取，取不到再从静态配置中读取
    :param config: 自定义的配置字典
    :return:
    """
    account_infos_api = config.get('account_infos_api') or ''
    if account_infos_api:
        headers = {"content-type": "application/json"}
        r = requests.get(account_infos_api, timeout=30, headers=headers)
        if r.status_code == 200:
            return eval(r.text)
    return config.get('account_infos') or []


def get_account_info(account_switching_type: str, account_infos: list) -> str:
    """
    获取账户信息
    :param account_switching_type: 账号切换类型：正序=asc，随机=random
    :param account_infos: openai的账号信息列表
    :return:
    """
    if len(account_infos or []) == 0:
        return ""
    if account_switching_type == AccountSwitchingType.ASC.value:
        record_file = 'curr_account_index.txt'
        record_value = u_file.read(record_file)
        curr_account_index = int(record_value) + 1 if record_value else 0
        curr_account_index = int(curr_account_index % len(account_infos))
        u_file.save(curr_account_index, record_file)
        return account_infos[curr_account_index]
    else:
        return random.choice(account_infos)


class GptHelper(object):
    """
    openai-gpt助手类
    """

    # 自定义配置
    config = eval(u_file.read('config.json')) or {}
    # 账号信息列表
    account_infos = get_account_infos(config)
    # 账号信息列表
    account_switching_type = config.get('account_switching_type') or 'asc'
    # 代理机器人
    account_info = get_account_info(account_switching_type=account_switching_type, account_infos=account_infos)
    chatbot = get_chatbot(account_info)

    def get_answer(self, prompt: str) -> str:
        """
        获取答案
        :param prompt: 问题内容
        :return:
        """
        try:
            print(f"Q：{prompt}")
            response = ""
            for data in self.chatbot.ask(prompt):
                response = data["message"]
            print(f"A：{response}")
            return response
        except Exception as e:
            msg = str(e).replace('\n', '').replace('\r', '')
            msg = f"请求错误，更换账号重试：{msg}"
            u_log.save_log(msg, 'error.log')
            account_info = get_account_info(account_switching_type=self.account_switching_type, account_infos=self.account_infos)
            self.chatbot = get_chatbot(account_info)
            return self.get_answer(prompt)
