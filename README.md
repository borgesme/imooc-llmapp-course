# imooc-llmapp-course

[慕课网 | AI Agent 全栈开发工程师](https://class.imooc.com/llmappdev)

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
