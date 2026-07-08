#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2026/7/9 0:08
@Author  : borgesme@gmail.com
@File    : 3.Pinecone删除数据.py
"""
import os

import dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

dotenv.load_dotenv()

# 读取环境变量配置
base_url = os.getenv("OPENAI_API_BASE_URL")
base_key = os.getenv("OPENAI_API_BASE_KEY")
base_model = os.getenv("OPENAI_API_BASE_MODEL")

embedding = OpenAIEmbeddings(model="text-embedding-3-small")
db = PineconeVectorStore(index_name="llmops", embedding=embedding, namespace="dataset")

id = "23cb7d6f-f77d-4465-8634-9c1ca7f93895"
db.delete([id], namespace="dataset")

# 获取实例
# pinecone_index = db.get_pinecone_index("llmops")
# pinecone_index.update(id="xxx", values=[], metadata={}, namespace="xxx")
