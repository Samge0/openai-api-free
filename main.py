#!/usr/bin/ruby
# -*- coding : utf-8 -*-
# author：samge
# data：2023-02-28 14:56
# describe：

from fastapi import Depends, FastAPI, Header

from models.m_openai import GptRequest
from utils import u_http, u_file, u_openai
from utils.u_openai import GptHelper

# api的简易token验证
access_token = eval(u_file.read('config.json')).get('auth_token')


async def verify_token(Authorization: str = Header(...)):
    """ token简易验证 """
    if Authorization != f"Bearer {access_token}":
        print(f"认证失败：{Authorization}")
        u_http.fail403(msg='Authorization header invalid')


app = FastAPI(dependencies=[Depends(verify_token)])
gptHelper = GptHelper()


@app.post("/ai/chat_free")
async def chat_free(request: GptRequest):
    result = gptHelper.get_answer(request.prompt)
    return u_http.success(result)
