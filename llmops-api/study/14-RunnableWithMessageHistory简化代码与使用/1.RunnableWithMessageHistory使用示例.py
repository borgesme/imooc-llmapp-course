#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2026/7/6 11:32
@Author  : borgesme@gmail.com
@File    : 1.RunnableWithMessageHistory使用示例.py
"""
import os
import warnings

# 过滤掉可能存在的其他残留弃用警告
warnings.filterwarnings("ignore", category=DeprecationWarning)

import dotenv
from langchain_community.chat_message_histories import FileChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

# 读取环境变量配置
base_url = os.getenv("OPENAI_API_BASE_URL")
base_key = os.getenv("OPENAI_API_BASE_KEY")
base_model = os.getenv("OPENAI_API_BASE_MODEL")

# 1.定义历史记忆存储
store = {}


# 2.工厂函数，用于获取指定会话的聊天历史
def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = FileChatMessageHistory(f"chat_history_{session_id}.txt")
    return store[session_id]


# 3.构建提示模板与大语言模型
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个强大的聊天机器人，请根据用户的需求回复问题。"),
    MessagesPlaceholder("history"),
    ("human", "{query}"),
])

llm = ChatOpenAI(model=base_model, base_url=base_url, api_key=base_key)

# 4.构建链
chain = prompt | llm | StrOutputParser()

# 5.包装链
with_message_chain = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="query",
    history_messages_key="history",
)

while True:
    query = input("Human: ")

    if query == "q":
        exit(0)

    # 6.运行链并传递配置信息
    response = with_message_chain.stream(
        {"query": query},
        config={"configurable": {"session_id": "muxiaoke"}}
    )
    print("AI: ", flush=True, end="")
    for chunk in response:
        print(chunk, flush=True, end="")
    print("")
