@echo off
cd /d "%LA_ROOT%"
"%LA_PYTHON%" "%LA_ROOT%\motor.py" reset
cd /d "%LA_SCENARIO%"
@echo on
@exit /b
