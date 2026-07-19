#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2026/7/19 0:40
@Author  : borgesme@gmail.com
@File    : api_tool_schema.py
"""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class ValidateOpenAPISchemaReq(FlaskForm):
    """校验OpenAPI规范字符串请求"""
    openapi_schema = StringField("openapi_schema", validators=[
        DataRequired(message="openapi_schema字符串不能为空")
    ])
