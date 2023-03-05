#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/3/4 23:05
# @Author  : Samge
import random
from revChatGPT.V1 import Chatbot

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


class GptHelper(object):
    account_infos = eval(u_file.read('config.json')).get('account_infos') or []
    chatbot = get_chatbot(random.choice(account_infos))

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
            msg = f"请求错误，更换账号重试：{e}"
            u_log.save_log(msg, 'error.log')
            self.chatbot = get_chatbot(random.choice(self.account_infos))
            return self.get_answer(prompt)
