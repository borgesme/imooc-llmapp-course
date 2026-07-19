#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2026/7/19 0:40
@Author  : borgesme@gmail.com
@File    : api_tool_service.py
"""
import json
from dataclasses import dataclass

from injector import inject

from internal.core.tools.api_tools.entities import OpenAPISchema
from internal.exception import (
    ValidateErrorException,
)


@inject
@dataclass
class ApiToolService:
    """自定义API插件服务"""

    @classmethod
    def parse_openapi_schema(cls, openapi_schema_str: str) -> OpenAPISchema:
        """解析传递的openapi_schema字符串，如果出错则抛出错误"""
        try:
            data = json.loads(openapi_schema_str.strip())
            if not isinstance(data, dict):
                raise
        except Exception as e:
            raise ValidateErrorException("传递数据必须符合OpenAPI规范的JSON字符串")

        return OpenAPISchema(**data)
