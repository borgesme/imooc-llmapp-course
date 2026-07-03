#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2026/7/3 0:32
@Author  : borgesme@gmail.com
@File    : http.py
"""
from flask import Flask

from config import Config
from internal.router import Router


class Http(Flask):
    """Http服务引擎"""

    def __init__(self, *args, conf: Config, router: Router, **kwargs):
        # 1.调用父类构造函数初始化
        super().__init__(*args, **kwargs)

        # 2.初始化应用配置
        self.config.from_object(conf)

        # 5.注册应用路由
        router.register_router(self)
