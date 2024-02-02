@echo off

REM Install Python with PATH
echo Installing Python...
start /wait "" https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe /quiet InstallAllUsers=1 PrependPath=1

REM Install required libraries
echo Installing required libraries...
pip install --upgrade pip
pip install time
pip install random

echo Installation complete.