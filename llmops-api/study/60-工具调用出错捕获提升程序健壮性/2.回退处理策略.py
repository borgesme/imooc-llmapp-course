#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2026/7/13 20:16
@Author  : borgesme@gmail.com
@File    : 2.回退处理策略.py
"""
import os

import dotenv
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

base_url = os.getenv("OPENAI_API_BASE_URL")
base_key = os.getenv("OPENAI_API_BASE_KEY")
base_model = os.getenv("OPENAI_API_BASE_MODEL")


@tool
def complex_tool(int_arg: int, float_arg: float, dict_arg: dict) -> int:
    """使用复杂工具进行复杂计算操作"""
    return int_arg * float_arg


# 1.创建大语言模型并绑定工具
llm = ChatOpenAI(model=base_model, base_url=base_url, api_key=base_key, temperature=0).bind_tools([complex_tool])
better_llm = ChatOpenAI(model="MiniMax-M3").bind_tools([complex_tool])

# 2.创建链并执行工具
better_chain = (better_llm | (lambda msg: msg.tool_calls[0]["args"]) | complex_tool)
chain = (llm | (lambda msg: msg.tool_calls[0]["args"]) | complex_tool).with_fallbacks([better_chain])

# 3.调用链
print(chain.invoke("使用复杂工具，对应参数为5和2.1，不要忘记了dict_arg参数"))
