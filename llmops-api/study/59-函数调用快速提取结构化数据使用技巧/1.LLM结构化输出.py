#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2026/7/13 19:42
@Author  : borgesme@gmail.com
@File    : 1.LLM结构化输出.py
"""
import os

import dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

dotenv.load_dotenv()

base_url = os.getenv("OPENAI_API_BASE_URL")
base_key = os.getenv("OPENAI_API_BASE_KEY")
base_model = os.getenv("OPENAI_API_BASE_MODEL")


class QAExtra(BaseModel):
    """一个问答键值对工具，传递对应的假设性问题+答案"""
    question: str = Field(description="假设性问题")
    answer: str = Field(description="假设性问题对应的答案")


llm = ChatOpenAI(model=base_model, base_url=base_url, api_key=base_key, temperature=0)
structured_llm = llm.with_structured_output(QAExtra, method="json_mode")

prompt = ChatPromptTemplate.from_messages([
    ("system", "请从用户传递的query中提取出假设性的问题+答案。响应格式为JSON，并携带`question`和`answer`两个字段。"),
    ("human", "{query}")
])

chain = {"query": RunnablePassthrough()} | prompt | structured_llm

print(chain.invoke("我叫慕小课，我喜欢打篮球，游泳。"))
