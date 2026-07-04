#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2026/7/4 17:01
@Author  : borgesme@gmail.com
@File    : 2.LCEL表达式简化版本.py
"""
import os

import dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

# 1.构建组件
prompt = ChatPromptTemplate.from_template("{query}")

# 2.创建大语言模型 (要不直接读取的环境变量中的base_url api_key)
base_url = os.getenv("OPENAI_API_BASE_URL")
base_key = os.getenv("OPENAI_API_BASE_KEY")
base_model = os.getenv("OPENAI_API_BASE_MODEL")

llm = ChatOpenAI(model=base_model, base_url=base_url, api_key=base_key)

# 3.创建字符串输出解析器
parser = StrOutputParser()

# 2.创建链
chain = prompt | llm | parser

# 3.调用链得到结果
print(chain.invoke({"query": "请讲一个程序员的冷笑话"}))
