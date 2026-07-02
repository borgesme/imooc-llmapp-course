#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2026/7/3 0:32
@Author  : borgesme@gmail.com
@File    : http.py
"""
from flask import Flask

from internal.router import Router


class Http(Flask):
    """Http服务引擎"""

    def __init__(self, *args, router: Router, **kwargs):
        # 1.调用父类构造函数初始化
        super().__init__(*args, **kwargs)

        # 5.注册应用路由
        router.register_router(self)
