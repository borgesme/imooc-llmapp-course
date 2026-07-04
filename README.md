# imooc-llmapp-course

[慕课网 | AI Agent 全栈开发工程师](https://class.imooc.com/llmappdev)

## 文档

> [langchain](https://reference.langchain.com/python/langchain/overview)
>
> [LangSmith platform](https://smith.langchain.com)

## python 虚拟环境

```bash
cd ./llmops-api

# 安装虚拟环境
python -m vnev env

# 激活虚拟环境
.\env\Scripts\activate

# 退出虚拟环境
.\env\Scripts\deactivate.

# 安装包
pip install openai
pip install langchain

# 更新镜像源 腾讯
pip config set global.index-url https://mirrors.cloud.tencent.com/pypi/simple/

# 查询验证
pip config list

# 查看用到的包
pip freeze

# 查看用到的包输入到文件（不建议）
pip freeze > requirements.txt

## 建议使用 https://pypi.org/project/pipreqs/
pip install --no-deps pipreqs
pip install yarg==0.1.9 docopt==0.6.2

# 依赖导入到requirements.txt
pipreqs --ignore venv --force
pipreqs --ignore venv --force --encoding=utf-8

# 根据requirements.txt安装依赖
pip install -r requirements.txt
```

## 数据库同步

```bash
# LLMOps项目运行命令
flask --app app.http.app db init

# 自动生成迁移脚本
flask --app app.http.app db migrate -m "create_table"

# 更新及回滚数据库
flask --app app.http.app db upgrade
flask --app app.http.app db downgrade

# 回退到最初的版本
flask --app app.http.app db downgrade base


# 回滚到特定的版本，可以在 downgrade 后带上特定的版本号，如下：
flask --app app.server.app db downgrade 版本号
```

## 安装 langchain

```bash
# pip uninstall langchain langchain-community -y
# 安装课程版本
# pip install langchain==0.2.1 langchain-community==0.2.1

# llmops-api\study\1-Prompt组件及使用技巧\4.复用提示模板.py
# 最新版本移除了 PipelinePromptTemplate
```
