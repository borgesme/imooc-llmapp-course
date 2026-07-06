#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2026/7/7 0:36
@Author  : borgesme@gmail.com
@File    : 1.Runnable重试机制.py
"""
from langchain_core.runnables import RunnableLambda

counter = -1


def func(x):
    global counter
    counter += 1
    print(f"当前的值为 {counter=}")
    return x / counter


chain = RunnableLambda(func).with_retry(stop_after_attempt=2)

resp = chain.invoke(2)

print(resp)
