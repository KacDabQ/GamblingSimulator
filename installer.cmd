@echo off

echo Installing Python...
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
del get-pip.py

echo Adding Python to PATH...
set "PYTHON_PATH=%~dp0\Scripts"
setx PATH "%PATH%;%PYTHON_PATH%" /M

echo ANY BUGS SHOULD BE REPORTED TO SAQREEZ!!!