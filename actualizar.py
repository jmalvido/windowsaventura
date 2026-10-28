"""Instalación y actualización completa desde GitHub. Solo biblioteca estándar."""
import contextlib,datetime,hashlib,json,os,re,shutil,stat,sys,tempfile,urllib.request,zipfile
from pathlib import Path,PurePosixPath,PureWindowsPath

DEFAULT_REPO='jmalvido/windowsaventura'  # Propuesto; publicar antes de descargar.
@contextlib.contextmanager
def lock_install(target):
    import msvcrt
    # Compartido por menú y actualizador; permanece fuera de la carpeta sustituida.
    p=target.parent/'.windowsaventura.lock'
    with p.open('a+b') as f:
        f.seek(0);f.write(b'0');f.flush();f.seek(0)
        try:msvcrt.locking(f.fileno(),msvcrt.LK_NBLCK,1)
        except OSError:raise RuntimeError('Cierra el juego y los otros actualizadores.')
        try:yield
        finally:f.seek(0);msvcrt.locking(f.fileno(),msvcrt.LK_UNLCK,1)
def safe_entries(z):
    seen=set()
    for i in z.infolist():
        p=PurePosixPath(i.filename); win=PureWindowsPath(i.filename)
        if p.is_absolute() or '..' in p.parts or win.drive or '\\' in i.filename or ':' in i.filename:
            raise ValueError('Ruta peligrosa en ZIP')
        if stat.S_ISLNK(i.external_attr>>16):raise ValueError('ZIP con enlaces')
        if any(x.rstrip(' .')!=x or x.split('.')[0].upper() in {'CON','PRN','AUX','NUL',*[f'COM{n}' for n in range(1,10)],*[f'LPT{n}' for n in range(1,10)]} for x in p.parts):
            raise ValueError('Nombre Windows no válido')
        k=i.filename.casefold().rstrip('/')
        if k in seen:raise ValueError('Nombre duplicado')
        seen.add(k)
        yield i
def unpack(archive,stage):
    with zipfile.ZipFile(archive) as z:
        entries=list(safe_entries(z))
        if sum(x.file_size for x in entries)>100_000_000:raise ValueError('ZIP demasiado grande')
        z.extractall(stage,members=entries)
    roots=[x for x in stage.iterdir() if x.is_dir()]
    if len(roots)!=1:raise ValueError('Se esperaba una carpeta raíz')
    source=roots[0]
    for name in ('jugar.bat','motor.py','menu.py','terminal.bat','catalogo.json','actividades','comandos'):
        if not (source/name).exists():raise ValueError('Paquete incompleto: '+name)
    catalog=json.loads((source/'catalogo.json').read_text(encoding='utf-8'))
    if catalog.get('schema')!=1 or not catalog.get('actividades'):raise ValueError('Catálogo no válido')
    for e in catalog['actividades']:
        if not re.fullmatch(r'actividad_[0-9]{3,}\.json',e['archivo']):raise ValueError('Actividad no válida')
        b=(source/'actividades'/e['archivo']).read_bytes()
        if hashlib.sha256(b).hexdigest()!=e['sha256']:raise ValueError('SHA-256 de actividad no coincide')
    return source
def install(source,target):
    if target.is_symlink() or (hasattr(target,'is_junction') and target.is_junction()):raise ValueError('Destino enlazado')
    if target.exists() and not (target/'jugar.bat').is_file():raise ValueError('La carpeta destino existe y no parece WindowsAventura')
    # El repositorio nunca aporta datos de alumnos.
    if (source/'datos').exists():shutil.rmtree(source/'datos')
    if (target/'datos').is_symlink() or (hasattr(target/'datos','is_junction') and (target/'datos').is_junction()):raise ValueError('Datos enlazados; revisar antes de actualizar')
    if (target/'datos').exists():
        for p in (target/'datos').rglob('*'):
            if p.is_symlink() or (hasattr(p,'is_junction') and p.is_junction()):raise ValueError('Datos con enlaces; revisar antes de actualizar')
        shutil.copytree(target/'datos',source/'datos')
    if (target/'config.json').exists():shutil.copy2(target/'config.json',source/'config.json')
    backup=target.with_name(target.name+'_copia_'+datetime.datetime.now().strftime('%Y%m%d_%H%M%S_%f'))
    had=target.exists()
    if had:target.rename(backup)
    try:source.rename(target)
    except Exception:
        if had:backup.rename(target)
        raise
    return backup if had else None
def main():
    if os.name!='nt':raise RuntimeError('Ejecuta este instalador desde CMD en Windows.')
    target=Path(os.environ['USERPROFILE'])/'windowsaventura'
    repo=DEFAULT_REPO
    if len(sys.argv)>1:repo=sys.argv[1]
    if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+',repo):raise ValueError('Repositorio inválido')
    target.parent.mkdir(parents=True,exist_ok=True)
    with lock_install(target),tempfile.TemporaryDirectory(prefix='wa-instalar-',dir=target.parent) as tmp:
        tmp=Path(tmp);archive=tmp/'juego.zip'
        url=f'https://github.com/{repo}/archive/refs/heads/main.zip'
        print('Descargando',repo,'(main)...')
        with urllib.request.urlopen(url,timeout=40) as response,archive.open('wb') as f:
            total=0
            while chunk:=response.read(65536):
                total+=len(chunk)
                if total>50_000_000:raise ValueError('Descarga demasiado grande')
                f.write(chunk)
        source=unpack(archive,tmp/'extraido')
        backup=install(source,target)
        print('Instalado en:',target)
        if backup:print('Copia anterior:',backup)
        print('Para jugar:',target/'jugar.bat')
if __name__=='__main__':
    try:main()
    except Exception as e:
        print('No se ha completado la actualización:',e)
        print('Comprueba que el repositorio esté publicado y cierra el juego.')
        sys.exit(1)
