#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2026/7/6 0:46
@Author  : borgesme@gmail.com
@File    : 1.实体记忆组件示例.py
"""
import os
import warnings

# 1. 过滤掉可能存在的其他残留弃用警告
warnings.filterwarnings("ignore", category=DeprecationWarning)

import dotenv
from langchain_classic.chains.conversation.base import ConversationChain
from langchain_classic.memory import ConversationEntityMemory
from langchain_classic.memory.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE
from langchain_community.chat_models.openai import ChatOpenAI

dotenv.load_dotenv()

# 读取环境变量配置
base_url = os.getenv("OPENAI_API_BASE_URL")
base_key = os.getenv("OPENAI_API_BASE_KEY")
base_model = os.getenv("OPENAI_API_BASE_MODEL")

llm = ChatOpenAI(model=base_model, base_url=base_url, api_key=base_key, temperature=0)
# llm = QianfanChatEndpoint()

chain = ConversationChain(
    llm=llm,
    prompt=ENTITY_MEMORY_CONVERSATION_TEMPLATE,
    memory=ConversationEntityMemory(llm=llm),
)

print(chain.invoke({"input": "你好，我是慕小课。我最近正在学习LangChain。"}))
print(chain.invoke({"input": "我最喜欢的编程语言是 Python。"}))
print(chain.invoke({"input": "我住在广州"}))

# 查询实体中的对话
res = chain.memory.entity_store.store
print(res)
