#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2026/7/9 23:48
@Author  : borgesme@gmail.com
@File    : 2.Office文档加载器.py
"""

import warnings

# 过滤langchain-community废弃警告
warnings.filterwarnings("ignore", category=DeprecationWarning)

# 需要安装 pip install unstructured openpyxl xlrd pandas
# pip install msoffcrypto-tool openpyxl xlrd

# 需要安装 pip install unstructured python-docx lxml

# 需要安装 pip install unstructured python-pptx lxml

from langchain_community.document_loaders import (
    # UnstructuredExcelLoader,
    # UnstructuredWordDocumentLoader,
    UnstructuredPowerPointLoader
)

# excel_loader = UnstructuredExcelLoader("./员工考勤表.xlsx", mode="elements")
# documents = excel_loader.load()

# word_loader = UnstructuredWordDocumentLoader("./喵喵.docx")
# documents = word_loader.load()

ppt_loader = UnstructuredPowerPointLoader("./章节介绍.pptx")
documents = ppt_loader.load()

print(documents)
print(len(documents))
print(documents[0].metadata)
