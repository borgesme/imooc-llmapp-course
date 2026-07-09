#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2026/7/9 23:49
@Author  : borgesme@gmail.com
@File    : 3.URL网页加载器.py
"""
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://imooc.com")
documents = loader.load()

print(documents)
print(len(documents))
print(documents[0].metadata)
print(documents[0].page_content)
