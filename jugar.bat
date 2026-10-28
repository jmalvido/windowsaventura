@echo off
setlocal DisableDelayedExpansion
chcp 65001 >nul
set "PYTHONUTF8=1"
set "PYTHONIOENCODING=utf-8"
py -3 -c "import sys;sys.exit(sys.version_info<(3,10))" >nul 2>&1
if not errorlevel 1 (
    py -3 "%~dp0menu.py"
    goto fin
)
python -c "import sys;sys.exit(sys.version_info<(3,10))" >nul 2>&1
if not errorlevel 1 (
    python "%~dp0menu.py"
    goto fin
)
echo Instala Python 3.10 o posterior desde https://www.python.org/downloads/windows/
echo Activa Add python.exe to PATH. Cierra y abre CMD despues.
:fin
pause
