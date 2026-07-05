#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2026/7/6 0:31
@Author  : borgesme@gmail.com
@File    : 1.摘要缓冲混合记忆示例.py.py
"""
import os
import warnings
from operator import itemgetter

import dotenv
from langchain_classic.memory import ConversationSummaryBufferMemory
from langchain_community.chat_models.openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough, RunnableLambda

# 1. 过滤掉可能存在的其他残留弃用警告
warnings.filterwarnings("ignore", category=DeprecationWarning)

dotenv.load_dotenv()

# 读取环境变量配置
base_url = os.getenv("OPENAI_API_BASE_URL")
base_key = os.getenv("OPENAI_API_BASE_KEY")
base_model = os.getenv("OPENAI_API_BASE_MODEL")

# 1.创建提示模板&记忆
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是OpenAI开发的聊天机器人，请根据对应的上下文回复用户问题"),
    MessagesPlaceholder("history"),  # 需要的history其实是一个列表
    ("human", "{query}"),
])
memory = ConversationSummaryBufferMemory(
    max_token_limit=300,
    return_messages=True,
    input_key="query",
    llm=ChatOpenAI(),
    # llm=QianfanChatEndpoint(),
)

# 2.创建大语言模型
llm = ChatOpenAI(model=base_model, base_url=base_url, api_key=base_key)
# llm = QianfanChatEndpoint()

# 3.构建链应用
chain = RunnablePassthrough.assign(
    history=RunnableLambda(memory.load_memory_variables) | itemgetter("history")
) | prompt | llm | StrOutputParser()

# 4.死循环构建对话命令行
while True:
    query = input("Human: ")

    if query == "q":
        exit(0)

    chain_input = {"query": query, "language": "中文"}

    response = chain.stream(chain_input)
    print("AI: ", flush=True, end="")
    output = ""
    for chunk in response:
        output += chunk
        print(chunk, flush=True, end="")
    memory.save_context(chain_input, {"output": output})
    print("")
    print("history: ", memory.load_memory_variables({}))
