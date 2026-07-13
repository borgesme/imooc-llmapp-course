#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2026/7/13 22:54
@Author  : borgesme@gmail.com
@File    : 1.预构建ReACT智能体.py
"""
import os

import dotenv
from langchain_community.tools.openai_dalle_image_generation import OpenAIDALLEImageGenerationTool
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from pydantic import BaseModel, Field

dotenv.load_dotenv()

base_url = os.getenv("OPENAI_API_BASE_URL")
base_key = os.getenv("OPENAI_API_BASE_KEY")
base_model = os.getenv("OPENAI_API_BASE_MODEL")


class GoogleSerperArgsSchema(BaseModel):
    query: str = Field(description="执行谷歌搜索的查询语句")


class DallEArgsSchema(BaseModel):
    query: str = Field(description="输入应该是生成图像的文本提示(prompt)")


search_wrapper = GoogleSerperAPIWrapper()
# 1.定义工具与工具列表
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

dalle = OpenAIDALLEImageGenerationTool(
    name="openai_dalle",
    api_wrapper=DallEAPIWrapper(model="dall-e-3"),
    args_schema=DallEArgsSchema,
)
tools = [google_serper, dalle]

# 2.创建大语言模型
model = ChatOpenAI(model=base_model, base_url=base_url, api_key=base_key, temperature=0)

# 3.使用预构建的函数创建ReACT智能体
agent = create_react_agent(model=model, tools=tools)

# 4.调用智能体并输出内容
print(agent.invoke({"messages": [("human", "请帮我绘制一幅鲨鱼在天上飞的图片")]}))
