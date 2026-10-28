@echo off
chcp 65001 >nul
title WindowsAventura - CMD
color 0B
prompt [WindowsAventura] $P$G
"%LA_PYTHON%" "%LA_ROOT%\motor.py" show
@echo on
