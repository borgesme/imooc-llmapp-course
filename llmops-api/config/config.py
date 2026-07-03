#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2026/7/3 10:55
@Author  : borgesme@gmail.com
@File    : config.py
"""


class Config:
    def __init__(self):
        # wft配置
        # 关闭wtf的csrf保护
        self.WTF_CSRF_ENABLED = False
