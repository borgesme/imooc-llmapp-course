#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2026/7/4 17:16
@Author  : borgesme@gmail.com
@File    : 1.RunnableParallel使用技巧.py
"""
import os

import dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

# 1.编排prompt
joke_prompt = ChatPromptTemplate.from_template("请讲一个关于{subject}的冷笑话，尽可能短一些")
poem_prompt = ChatPromptTemplate.from_template("请写一篇关于{subject}的诗，尽可能短一些")

# 2.创建大语言模型 (要不直接读取的环境变量中的base_url api_key)
base_url = os.getenv("OPENAI_API_BASE_URL")
base_key = os.getenv("OPENAI_API_BASE_KEY")
base_model = os.getenv("OPENAI_API_BASE_MODEL")

llm = ChatOpenAI(model=base_model, base_url=base_url, api_key=base_key)

# 3.创建字符串输出解析器
parser = StrOutputParser()

# 4.编排链
joke_chain = joke_prompt | llm | parser
poem_chain = poem_prompt | llm | parser

# 5.并行链
map_chain = RunnableParallel(joke=joke_chain, poem=poem_chain)
# map_chain = RunnableParallel({
#     "joke": joke_chain,
#     "poem": poem_chain,
# })

# 6.调用链得到结果
res = map_chain.invoke({"subject": "程序员"})

print(res)
