#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2026/7/4 17:43
@Author  : borgesme@gmail.com
@File    : 1.回调功能使用技巧.py
"""
import os
import time
from typing import Dict, Any, List, Optional
from uuid import UUID

import dotenv
from langchain_core.callbacks import StdOutCallbackHandler, BaseCallbackHandler
from langchain_core.messages import BaseMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.outputs import LLMResult
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()


class LLMOpsCallbackHandler(BaseCallbackHandler):
    """自定义LLMOps回调处理器"""
    start_at: float = 0

    def on_chat_model_start(
            self,
            serialized: Dict[str, Any],
            messages: List[List[BaseMessage]],
            *,
            run_id: UUID,
            parent_run_id: Optional[UUID] = None,
            tags: Optional[List[str]] = None,
            metadata: Optional[Dict[str, Any]] = None,
            **kwargs: Any,
    ) -> Any:
        print("聊天模型开始执行了")
        print("serialized:", serialized)
        print("messages:", messages)
        self.start_at = time.time()

    def on_llm_end(
            self,
            response: LLMResult,
            *,
            run_id: UUID,
            parent_run_id: Optional[UUID] = None,
            **kwargs: Any,
    ) -> Any:
        end_at: float = time.time()
        print("完整输出:", response)
        print("程序消耗:", end_at - self.start_at)


# 1.编排prompt
prompt = ChatPromptTemplate.from_template("{query}")

# 2.创建大语言模型 (要不直接读取的环境变量中的base_url api_key)
base_url = os.getenv("OPENAI_API_BASE_URL")
base_key = os.getenv("OPENAI_API_BASE_KEY")
base_model = os.getenv("OPENAI_API_BASE_MODEL")

llm = ChatOpenAI(model=base_model, base_url=base_url, api_key=base_key)

# 3.创建字符串输出解析器
parser = StrOutputParser()

# 4.编排链
chain = {"query": RunnablePassthrough()} | prompt | llm | parser

# 6.调用链并执行
resp = chain.stream(
    "你好，你是？",
    config={"callbacks": [StdOutCallbackHandler(), LLMOpsCallbackHandler()]}
)

for chunk in resp:
    pass
