@echo off
setlocal DisableDelayedExpansion
chcp 65001 >nul
set "PYTHONUTF8=1"
set "PYTHONIOENCODING=utf-8"
rem Repositorio propuesto: publicar antes de usar.
set "WA_REPO=jmalvido/windowsaventura"
set "WA_TMP=%TEMP%\wa_actualizar_%RANDOM%_%RANDOM%.py"
py -3 -c "import sys;sys.exit(sys.version_info<(3,10))" >nul 2>&1
if not errorlevel 1 (
    set "WA_PY=py -3"
    goto descargar
)
python -c "import sys;sys.exit(sys.version_info<(3,10))" >nul 2>&1
if not errorlevel 1 (
    set "WA_PY=python"
    goto descargar
)
echo Instala Python 3.10 o posterior y vuelve a abrir CMD.
goto fin
:descargar
cd /d "%USERPROFILE%"
curl.exe -fL --proto "=https" --connect-timeout 20 --max-time 90 "https://raw.githubusercontent.com/%WA_REPO%/main/actualizar.py" -o "%WA_TMP%"
if errorlevel 1 (
    echo No se pudo descargar el actualizador. La instalacion no se ha modificado.
    goto limpiar
)
%WA_PY% "%WA_TMP%" "%WA_REPO%"
:limpiar
if exist "%WA_TMP%" del "%WA_TMP%"
:fin
pause
