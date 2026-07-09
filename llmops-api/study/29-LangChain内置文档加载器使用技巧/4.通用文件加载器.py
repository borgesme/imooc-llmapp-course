#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2026/7/9 23:49
@Author  : borgesme@gmail.com
@File    : 4.通用文件加载器.py
"""
from langchain_community.document_loaders import UnstructuredFileLoader

loader = UnstructuredFileLoader("./项目API资料.md")
documents = loader.load()

print(documents)
print(len(documents))
print(documents[0].metadata)
