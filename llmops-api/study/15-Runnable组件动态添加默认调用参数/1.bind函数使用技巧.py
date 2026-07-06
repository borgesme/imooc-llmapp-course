#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2026/7/6 23:40
@Author  : borgesme@gmail.com
@File    : 1.bind函数使用技巧.py
"""
import os

import dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

# 读取环境变量配置
base_url = os.getenv("OPENAI_API_BASE_URL")
base_key = os.getenv("OPENAI_API_BASE_KEY")
base_model = os.getenv("OPENAI_API_BASE_MODEL")

prompt = ChatPromptTemplate.from_messages([
    ("human", "{query}")
])

llm = ChatOpenAI(model=base_model, base_url=base_url, api_key=base_key)

chain = prompt | llm.bind(model="MiniMax-M2.7") | StrOutputParser()

content = chain.invoke({"query": "你是什么模型呢？"})

print(content)
