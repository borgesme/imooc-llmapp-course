#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2026/7/8 23:25
@Author  : borgesme@gmail.com
@File    : 1.faiss向量数据库使用示例.py
"""
import os

import dotenv
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

dotenv.load_dotenv()

# 读取环境变量配置
base_url = os.getenv("OPENAI_API_BASE_URL")
base_key = os.getenv("OPENAI_API_BASE_KEY")
base_model = os.getenv("OPENAI_API_BASE_MODEL")

embedding = OpenAIEmbeddings(
    model="text-embedding-3-small",
    base_url=base_url,
    api_key=base_key,
)

db = FAISS.load_local(
    "./vector-store/",
    embedding,
    allow_dangerous_deserialization=True
)

print(db.similarity_search_with_score("我养了一只猫，叫笨笨"))
