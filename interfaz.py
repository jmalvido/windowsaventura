"""Colores ANSI en consola de Windows con degradación a texto."""
import os,re,sys
def terminal():
    if not sys.stdout.isatty() or 'NO_COLOR' in os.environ:return False
    if os.name=='nt':
        import ctypes
        from ctypes import wintypes
        k=ctypes.windll.kernel32
        k.GetStdHandle.restype=wintypes.HANDLE
        k.GetConsoleMode.argtypes=[wintypes.HANDLE,ctypes.POINTER(wintypes.DWORD)]
        k.SetConsoleMode.argtypes=[wintypes.HANDLE,wintypes.DWORD]
        handle=k.GetStdHandle(-11); mode=ctypes.c_ulong()
        return bool(k.GetConsoleMode(handle,ctypes.byref(mode)) and k.SetConsoleMode(handle,mode.value|4))
    return os.environ.get('TERM','') not in ('','dumb')
COLORS={'title':'1;36','command':'1;33','success':'1;32','error':'1;31','hint':'1;35','muted':'36'}
def color(text,role='command'):
    return '\033['+COLORS[role]+'m'+str(text)+'\033[0m' if terminal() else str(text)
def clear():
    if sys.stdout.isatty() and os.environ.get('LA_CLEAR','1')!='0':
        if os.name=='nt':os.system('cls')
        else:print('\033[2J\033[H',end='',flush=True)
def highlight(text):
    return re.sub(r'\b(?:PISTA|COMPROBAR|AYUDA|REINICIAR|MENU|ACTUALIZAR|SALIR|IDIOMA|CD|DIR|TYPE|MD|COPY|MOVE|REN|HELP|CLS|VER|DATE|TIME|TITLE|COLOR|PROMPT|PATH|START|CMD|EXIT|VOL|LABEL|CHKDSK|SHUTDOWN|SYSTEMINFO|CALL|ECHO)\b',lambda m:color(m.group()),str(text))
def pause(message):input(message)
