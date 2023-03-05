#!/usr/bin/ruby
# -*- coding : utf-8 -*-
# author：samge
# data：2023-02-28 15:11
# describe：
from typing import Optional
from pydantic import BaseModel


class GptRequest(BaseModel):
    """请求体"""
    prompt: str  # 数据来源 ： 7为中国供应商
