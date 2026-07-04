#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2026/7/4 10:32
@Author  : borgesme@gmail.com
@File    : 4.复用提示模板-new.py
"""

# LangChain 官方推荐中，PipelinePromptTemplate 已经逐渐被 LCEL (LangChain Expression Language) 语法所取代
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableLambda

full_template = PromptTemplate.from_template("""{instruction}

{example}

{start}""")

# 描述模板
instruction_prompt = PromptTemplate.from_template("你正在模拟{person}")

# 示例模板
example_prompt = PromptTemplate.from_template("""下面是一个交互例子：

Q: {example_q}
A: {example_a}""")

# 开始模板
start_prompt = PromptTemplate.from_template("""现在，你是一个真实的人，请回答用户的问题:

Q: {input}
A:""")

# 2. 用 LCEL 像拼积木一样把它们连起来
# 这里利用 RunnablePassthrough 来承接输入变量，并顺次格式化拼接
# 2. 在 lambda 拼接时，显式地在各个模板之间加上 \n\n
composed_chain = (
        RunnablePassthrough()
        | RunnableLambda(
    lambda x: f"{instruction_prompt.format(**x)}\n\n{example_prompt.format(**x)}\n\n{start_prompt.format(**x)}")
)

# 3. 运行得到拼接后的完整字符串
result = composed_chain.invoke({
    "person": "雷军",
    "example_q": "你最喜欢的汽车是什么?",
    "example_a": "小米su7",
    "input": "你最喜欢的手机是什么?"
})
print(result)
