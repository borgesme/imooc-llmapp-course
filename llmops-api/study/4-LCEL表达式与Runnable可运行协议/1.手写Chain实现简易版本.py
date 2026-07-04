#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2026/7/4 16:46
@Author  : borgesme@gmail.com
@File    : 1.手写Chain实现简易版本.py
"""
import os
from typing import Any

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


# 2.定义一个链
class Chain:
    steps: list = []

    def __init__(self, steps: list):
        self.steps = steps

    def invoke(self, input: Any) -> Any:
        for step in self.steps:
            input = step.invoke(input)
            print("步骤:", step)
            print("输出:", input)
            print("===============")
        return input


# 3.编排链
chain = Chain([prompt, llm, parser])

# 4.执行链并获取结果
print(chain.invoke({"query": "你好，你是?"}))
