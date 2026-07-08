#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2026/7/8 15:33
@Author  : borgesme@gmail.com
@File    : 01. OpenAI嵌入模型示例.py
"""
import os

import dotenv
import numpy as np
from langchain_openai import OpenAIEmbeddings
from numpy.linalg import norm

dotenv.load_dotenv()

# 读取环境变量配置
base_url = os.getenv("OPENAI_API_BASE_URL")
base_key = os.getenv("OPENAI_API_BASE_KEY")
base_model = os.getenv("OPENAI_API_BASE_MODEL")


def cosine_similarity(vec1: list, vec2: list) -> float:
    """计算传入两个向量的余弦相似度"""
    # 1.计算两个向量的点积
    dot_product = np.dot(vec1, vec2)

    # 2.计算向量的长度
    vec1_norm = norm(vec1)
    vec2_norm = norm(vec2)

    # 3.计算余弦相似度
    return dot_product / (vec1_norm * vec2_norm)


# 1.创建文本嵌入模型
embeddings = OpenAIEmbeddings(
    model="moonshot-embedding",
    base_url=base_url,
    api_key=base_key,
)

# 2.嵌入文本
query_vector = embeddings.embed_query("我叫慕小课，我喜欢打篮球")

print(query_vector)
print(len(query_vector))

# 3.嵌入文档列表/字符串列表
documents_vector = embeddings.embed_documents([
    "我叫慕小课，我喜欢打篮球",
    "这个喜欢打篮球的人叫慕小课",
    "求知若渴，虚心若愚"
])
print(len(documents_vector))

# 4.计算余弦相似度
print("向量1和向量2的相似度:", cosine_similarity(documents_vector[0], documents_vector[1]))
print("向量1和向量3的相似度:", cosine_similarity(documents_vector[0], documents_vector[2]))
