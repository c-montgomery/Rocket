@echo off
cd /d "%~dp0"
python -m pip install -q -r requirements.txt
cd pygame_test
python pygame_test.py
