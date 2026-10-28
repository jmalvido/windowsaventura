@echo off
"%LA_PYTHON%" "%LA_ROOT%\motor.py" remember "%CD%"
type nul > "%LA_ROOT%\datos\salir.flag"
exit
