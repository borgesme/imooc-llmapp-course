#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2026/7/10 3:35
@Author  : borgesme@gmail.com
@File    : 1.语义分割器使用示例.py
"""
import dotenv
from langchain_community.document_loaders import UnstructuredFileLoader
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings

dotenv.load_dotenv()

# 1.构建加载器和文本分割器
loader = UnstructuredFileLoader("./科幻短篇.txt")
text_splitter = SemanticChunker(
    embeddings=OpenAIEmbeddings(model="text-embedding-3-small"),
    number_of_chunks=10,
    add_start_index=True,
    sentence_split_regex=r"(?<=[。？！.?!])"
)

# 2.加载文本与分割
documents = loader.load()
chunks = text_splitter.split_documents(documents)

# 3.循环打印
for chunk in chunks:
    print(f"块大小: {len(chunk.page_content)}, 元数据: {chunk.metadata}")
