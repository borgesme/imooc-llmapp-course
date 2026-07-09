#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2026/7/10 0:35
@Author  : borgesme@gmail.com
@File    : 3.GenericLoader示例.py
"""
from langchain_community.document_loaders.generic import GenericLoader

loader = GenericLoader.from_filesystem(".", glob="*.txt", show_progress=True)

for idx, doc in enumerate(loader.lazy_load()):
    print(f"当前正在加载第{idx}个文件,文件名:{doc.metadata['source']}")
