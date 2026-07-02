#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2026/7/3 0:21
@Author  : borgesme@gmail.com
@File    : router.py
"""
from dataclasses import dataclass

from flask import Flask, Blueprint
from injector import inject

from internal.handler import AppHandler


@inject
@dataclass
class Router:
    """路由"""
    app_handler: AppHandler

    def register_router(self, app: Flask):
        """注册路由"""
        # 1.创建一个蓝图
        bp = Blueprint("llmops", __name__, url_prefix="")

        # 2.将url与对应的控制器方法做绑定
        bp.add_url_rule("/ping", view_func=self.app_handler.ping)

        # 3.在应用上去注册蓝图
        app.register_blueprint(bp)
