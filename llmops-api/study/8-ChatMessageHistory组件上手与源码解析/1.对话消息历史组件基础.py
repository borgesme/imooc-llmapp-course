#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2026/7/5 23:04
@Author  : borgesme@gmail.com
@File    : 1.对话消息历史组件基础.py
"""
from langchain_core.chat_history import InMemoryChatMessageHistory

chat_history = InMemoryChatMessageHistory()

chat_history.add_user_message("你好，我是慕小课，你是谁？")
chat_history.add_ai_message("你好，我是ChatGPT，有什么可以帮到您的？")

print(chat_history.messages)
