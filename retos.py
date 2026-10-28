"""Validación de CMD. No ejecuta scripts ni órdenes extraídas del JSON."""
import os,subprocess
QUERIES={'version':'ver','volumen':'vol %SystemDrive%','fecha':'date /t','equipo':'echo %COMPUTERNAME%'}
def query(name):
    if os.name!='nt':raise OSError('La consulta real necesita Windows')
    p=subprocess.run([os.environ['COMSPEC'],'/d','/u','/c',QUERIES[name]],capture_output=True,timeout=15)
    if p.returncode:raise OSError('No se pudo consultar '+name)
    return p.stdout.decode('utf-16-le').strip()
def read_text(p):
    raw=p.read_bytes()
    if raw.startswith((b'\xff\xfe',b'\xfe\xff')):return raw.decode('utf-16')
    if b'\0' in raw:return raw.decode('utf-16-le')
    try:return raw.decode('utf-8-sig')
    except UnicodeDecodeError:return raw.decode('oem' if os.name=='nt' else 'cp850')
def normalize(text):return ' '.join(text.split()).casefold()
def check(t,a,s,w,answer,loc,safe):
    kind=t['tipo']
    if kind=='respuesta_sistema':
        return normalize(answer(loc(t['pregunta'])+' '))==normalize(query(t['consulta']))
    if kind=='salida':
        p=safe(w,t['ruta'])
        return p.is_file() and not p.is_symlink() and normalize(read_text(p))==normalize(query(t['consulta']))
    if kind=='entorno':
        return os.environ.get(t['nombre'],'').casefold()==t['valor'].casefold()
    if kind=='texto':
        p=safe(w,t['ruta'])
        if not p.is_file() or p.is_symlink():return False
        lines=[normalize(x) for x in read_text(p).splitlines() if x.strip()]
        return lines==[normalize(x) for x in t['lineas']]
    if kind=='reentrada':
        return bool(s.get('sesion_paso')) and s['sesion_paso']!=os.environ.get('LA_SESSION_ID','') and bool(os.environ.get('LA_SESSION_ID'))
    return False
