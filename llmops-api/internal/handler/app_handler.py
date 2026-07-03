#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2026/7/3 0:18
@Author  : borgesme@gmail.com
@File    : app_handler.py
"""
import os

from openai import OpenAI

from schema.app_schema import CompletionReq


class AppHandler:
    """应用控制器"""

    def completion(self):
        """聊天接口"""
        # 1.提取从接口中获取的输入，POST
        req = CompletionReq()
        if not req.validate():
            return req.errors

        # 2.构建OpenAI客户端，并发起请求
        base_url = os.getenv("OPENAI_API_BASE_URL")
        base_key = os.getenv("OPENAI_API_BASE_KEY")
        base_model = os.getenv("OPENAI_API_BASE_MODEL")

        client = OpenAI(
            base_url=base_url,
            api_key=base_key,
        )

        print('111_api_url', base_url)
        print('222_api_key', base_key)
        print('333_api_model', base_model)

        # 3.得到请求响应，然后将OpenAI的响应传递给前端
        completion = client.chat.completions.create(
            model=base_model,
            messages=[
                {"role": "system", "content": "你是OpenAI开发的聊天机器人，请根据用户的输入回复对应的信息"},
                {"role": "user", "content": req.query.data},
            ]
        )

        content = completion.choices[0].message.content

        return content

    def ping(self):
        return {"ping": "pong"}
