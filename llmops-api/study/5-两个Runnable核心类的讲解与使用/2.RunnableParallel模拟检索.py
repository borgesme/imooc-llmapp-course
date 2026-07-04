#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2026/7/4 17:26
@Author  : borgesme@gmail.com
@File    : 2.RunnableParallel模拟检索.py
"""
import os
from operator import itemgetter

import dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()


def retrieval(query: str) -> str:
    """一个模拟的检索器函数"""
    print("正在检索:", query)
    return "我是慕小课"


# 1.编排prompt
prompt = ChatPromptTemplate.from_template("""请根据用户的问题回答，可以参考对应的上下文进行生成。

<context>
{context}
</context>

用户的提问是: {query}""")

# 2.创建大语言模型 (要不直接读取的环境变量中的base_url api_key)
base_url = os.getenv("OPENAI_API_BASE_URL")
base_key = os.getenv("OPENAI_API_BASE_KEY")
base_model = os.getenv("OPENAI_API_BASE_MODEL")

llm = ChatOpenAI(model=base_model, base_url=base_url, api_key=base_key)

# 3.创建字符串输出解析器
parser = StrOutputParser()

# 4.编排链
chain = {
            "context": lambda x: retrieval(x["query"]),
            "query": itemgetter("query"),
        } | prompt | llm | parser

# 6.调用链得到结果
content = chain.invoke({"query": "你好，我是谁?"})

print(content)
