#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2026/7/10 0:35
@Author  : borgesme@gmail.com
@File    : 2.FileSystemBlobLoader示例.py
"""
from langchain_community.document_loaders.blob_loaders import FileSystemBlobLoader

loader = FileSystemBlobLoader(".", show_progress=True)

for blob in loader.yield_blobs():
    print(blob.as_string())
