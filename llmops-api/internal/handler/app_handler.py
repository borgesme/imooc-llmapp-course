#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2026/7/3 0:18
@Author  : borgesme@gmail.com
@File    : app_handler.py
"""
import os

from flask import request
from openai import OpenAI


class AppHandler:
    """应用控制器"""

    def completion(self):
        """聊天接口"""
        # 1.提取从接口中获取的输入，POST
        query = request.json.get("query")

        # 2.构建OpenAI客户端，并发起请求
        client = OpenAI(
            base_url="https://api.minimaxi.com/v1",
            api_key="sk-api-1QeY3w4fiZs8vf4420OUkuvh3rTFowsoCH1UfJHpxOjAm4a7OVOK1coDkYfo8voBU4jVh22DshndgYOuUj2Pp5fXp7PQIRAZLjJE94avgJt_AMjktIjn",
            # base_url=os.getenv("OPENAI_BASE_URL"),
            # api_key=os.getenv("OPENAI_API_KEY"),
        )

        print('111', os.getenv("OPENAI_BASE_URL"))
        print('222', os.getenv("OPENAI_API_KEY"))

        # 3.得到请求响应，然后将OpenAI的响应传递给前端
        completion = client.chat.completions.create(
            model="MiniMax-M3",
            messages=[
                {"role": "system", "content": "你是OpenAI开发的聊天机器人，请根据用户的输入回复对应的信息"},
                {"role": "user", "content": query},
            ]
        )

        content = completion.choices[0].message.content

        return content

    def ping(self):
        return {"ping": "pong"}
