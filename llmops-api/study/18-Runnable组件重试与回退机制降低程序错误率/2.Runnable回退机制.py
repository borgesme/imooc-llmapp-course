#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2026/7/7 0:36
@Author  : borgesme@gmail.com
@File    : 2.Runnable回退机制.py
"""
import os

import dotenv
from langchain_community.chat_models.minimax import MiniMaxChat
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

# 读取环境变量配置
base_url = os.getenv("OPENAI_API_BASE_URL")
base_key = os.getenv("OPENAI_API_BASE_KEY")
base_model = os.getenv("OPENAI_API_BASE_MODEL")

# 1.构建prompt与LLM，并将model切换为gpt-3.5-turbo-18k引发出错
prompt = ChatPromptTemplate.from_template("{query}")
llm = ChatOpenAI(model="gpt-3.5-turbo-18k", base_url=base_url, api_key=base_key).with_fallbacks(
    [
        MiniMaxChat(api_key=base_key, )
    ]
)

# 2.构建链应用
chain = prompt | llm | StrOutputParser()

# 3.调用链并输出结果
content = chain.invoke({"query": "你好，你是?"})
print(content)
