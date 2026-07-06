#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2026/7/7 0:22
@Author  : borgesme@gmail.com
@File    : 1.多LLM链选择示例.py
"""
import os
import warnings

# 1. 过滤掉可能存在的其他残留弃用警告
warnings.filterwarnings("ignore", category=DeprecationWarning)

import dotenv
from langchain_community.chat_models.moonshot import MoonshotChat
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import ConfigurableField
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

# 读取环境变量配置
base_url = os.getenv("OPENAI_API_BASE_URL")
base_key = os.getenv("OPENAI_API_BASE_KEY")
base_model = os.getenv("OPENAI_API_BASE_MODEL")

# 1.创建提示模板&定义默认大语言模型
prompt = ChatPromptTemplate.from_template("{query}")
llm = ChatOpenAI(model=base_model, base_url=base_url, api_key=base_key).configurable_alternatives(
    ConfigurableField(id="llm"),
    default_key="MiniMax-M2.7",
    kimi=ChatOpenAI(model="MiniMax-M2.7", base_url=base_url, api_key=base_key),
    moonshot=MoonshotChat(),
)

# 2.构建链应用
chain = prompt | llm | StrOutputParser()

# 3.调用链并传递配置信息，并切换到文心一言模型或者gpt4模型
content = chain.invoke(
    {"query": "你好，你是什么模型呢?"},
    config={"configurable": {"llm": "kimi-k2.7"}}
)
print(content)
