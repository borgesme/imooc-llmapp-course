#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2026/7/9 23:47
@Author  : borgesme@gmail.com
@File    : 1.Markdown文档加载器.py
"""

# 需要安装 pip install unstructured markdown unstructured[md]
from langchain_community.document_loaders import UnstructuredMarkdownLoader

loader = UnstructuredMarkdownLoader("./项目API资料.md")
documents = loader.load()

print(documents)
print(len(documents))
print(documents[0].metadata)
print(documents[0].page_content)
