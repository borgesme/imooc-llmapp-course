#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2026/7/3 0:12
@Author  : borgesme@gmail.com
@File    : test.py
"""
from injector import Injector, inject


class A:
    name: str = "llmops"


@inject
class B:
    def __init__(self, a: A):
        self.a = a

    def print(self):
        print(f"Class A 的 name: {self.a.name}")


injector = Injector()
b_instance = injector.get(B)
b_instance.print()
