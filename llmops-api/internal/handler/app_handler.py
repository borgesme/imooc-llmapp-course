#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2026/7/3 0:18
@Author  : borgesme@gmail.com
@File    : app_handler.py
"""
import os
import uuid
import warnings
from dataclasses import dataclass
from operator import itemgetter
from typing import Any, Dict
from uuid import UUID

# 过滤掉可能存在的其他残留弃用警告
warnings.filterwarnings("ignore", category=DeprecationWarning)

from injector import inject
from langchain_classic.memory import ConversationBufferWindowMemory
from langchain_community.chat_message_histories import FileChatMessageHistory
from langchain_classic.base_memory import BaseMemory

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough, RunnableLambda, RunnableConfig
from langchain_core.tracers import Run
from langchain_openai import ChatOpenAI

from internal.schema.app_schema import CompletionReq
from internal.service import AppService
from pkg.response import success_json, validate_error_json, success_message


@inject
@dataclass
class AppHandler:
    """应用控制器"""
    app_service: AppService

    def create_app(self):
        """调用服务创建新的APP记录"""
        app = self.app_service.create_app()
        return success_message(f"应用已经成功创建，id为{app.id}")

    def get_app(self, id: uuid.UUID):
        app = self.app_service.get_app(id)
        return success_message(f"应用已经成功获取，名字是{app.name}")

    def update_app(self, id: uuid.UUID):
        app = self.app_service.update_app(id)
        return success_message(f"应用已经成功修改，修改的名字是:{app.name}")

    def delete_app(self, id: uuid.UUID):
        app = self.app_service.delete_app(id)
        return success_message(f"应用已经成功删除，id为:{app.id}")

    @classmethod
    def _load_memory_variables(cls, input: Dict[str, Any], config: RunnableConfig) -> Dict[str, Any]:
        """加载记忆变量信息"""
        # 1.从 config 中获取 configurable
        configurable = config.get("configurable", {})
        configurable_memory = configurable.get("memory", None)
        if configurable_memory is not None and isinstance(configurable_memory, BaseMemory):
            return configurable_memory.load_memory_variables(input)
        return {"history": []}

    @classmethod
    def _save_context(cls, run_obj: Run, config: RunnableConfig) -> None:
        """存储对应的上下文信息到记忆实体中"""
        configurable = config.get("configurable", {})
        configurable_memory = configurable.get("memory", None)
        if configurable_memory is not None and isinstance(configurable_memory, BaseMemory):
            configurable_memory.save_context(run_obj.inputs, run_obj.outputs)

    def debug(self, app_id: UUID):
        """聊天接口"""
        # 1.提取从接口中获取的输入，POST
        req = CompletionReq()
        if not req.validate():
            return validate_error_json(req.errors)

        # 2. 创建 prompt 与记忆
        system_prompt = "你是一个强大的聊天机器人，能根据用户的提问回复对应的问题"
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder("history"),
            ("human", "{query}"),
        ])

        memory = ConversationBufferWindowMemory(
            k=3,
            input_key="query",
            output_key="output",
            return_messages=True,
            chat_memory=FileChatMessageHistory("./storage/memory/chat_history.txt"),
        )

        # 构建OpenAI客户端，并发起请求
        base_url = os.getenv("OPENAI_API_BASE_URL")
        base_key = os.getenv("OPENAI_API_BASE_KEY")
        base_model = os.getenv("OPENAI_API_BASE_MODEL")

        # 3.创建llm
        llm = ChatOpenAI(model=base_model, base_url=base_url, api_key=base_key)

        # 4.创建链应用
        chain = (RunnablePassthrough.assign(
            history=RunnableLambda(self._load_memory_variables) | itemgetter("history")
        ) | prompt | llm | StrOutputParser()).with_listeners(on_end=self._save_context)

        # 5.调用链生成内容
        chain_input = {"query": req.query.data}
        content = chain.invoke(chain_input, config={"configurable": {"memory": memory}})

        return success_json({"content": content})

    def ping(self):
        return success_json()
        # raise FailException("数据未找到")
        # return {"ping": "pong"}
