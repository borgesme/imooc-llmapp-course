#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2026/7/13 17:39
@Author  : borgesme@gmail.com
@File    : google_serper_tool.py
"""
import dotenv
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_core.tools import Tool
from pydantic import BaseModel, Field


class GoogleSerperArgsSchema(BaseModel):
    query: str = Field(description="执行谷歌搜索的查询语句")


dotenv.load_dotenv()

# 3. 初始化底层的 Serper API 包装器
search_wrapper = GoogleSerperAPIWrapper()

google_serper = Tool(
    name="google_serper",
    func=search_wrapper.run,  # 直接映射执行函数
    description=(
        "一个低成本的谷歌搜索API。"
        "当你需要回答有关时事的问题时，可以调用该工具。"
        "该工具的输入是搜索查询语句。"
    ),
    args_schema=GoogleSerperArgsSchema,
)

print(google_serper.invoke("马拉松的世界纪录是多少?"))
