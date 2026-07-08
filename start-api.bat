@echo off
:: 进入llmops-api目录
cd /d ./llmops-api

:: 激活venv虚拟环境并启动flask
call .\env\Scripts\activate.bat
python.exe -m flask run

:: 运行结束暂停窗口，方便看报错
pause
