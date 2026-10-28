#!/usr/bin/env python3
"""WindowsAventura 0.1 — CMD real, Python 3.10+, sin dependencias."""
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sys
import tempfile
import urllib.request
import interfaz as ui

ROOT = Path(__file__).resolve().parent
DATA = ROOT / 'datos'
CATALOG = ROOT / 'actividades'

def read(p):
    return json.loads(Path(p).read_text(encoding='utf-8'))

def write(p, value):
    p = Path(p)
    p.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=p.parent, prefix='.guardado-')
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            json.dump(value, f, ensure_ascii=False, indent=2)
            f.write('\n')
        os.replace(tmp, p)
    finally:
        if os.path.exists(tmp): os.unlink(tmp)

def settings():
    return read(DATA/'preferencias.json') if (DATA/'preferencias.json').exists() else {'idioma':'es'}

def lang(): return settings()['idioma']
def tr(es, eu): return eu if lang() == 'eu' else es
def loc(value, language=None):
    return value[language or lang()] if isinstance(value, dict) else value

def safe(base, relative):
    if not isinstance(relative, str) or not relative or Path(relative).is_absolute() or '..' in Path(relative).parts:
        raise ValueError('Ruta no válida / Bide baliogabea')
    from pathlib import PureWindowsPath
    win=PureWindowsPath(relative)
    if win.drive or win.root or ':' in relative or '\\' in relative or any(x.rstrip(' .') != x or x.split('.')[0].upper() in {'CON','PRN','AUX','NUL',*[f'COM{i}' for i in range(1,10)],*[f'LPT{i}' for i in range(1,10)]} for x in win.parts):
        raise ValueError('Ruta Windows no válida / Windows bide baliogabea')
    p = base / relative
    try:
        p.resolve().relative_to(base.resolve())
    except ValueError:
        raise ValueError('Ruta fuera del escenario / Eszenatokitik kanpoko bidea')
    return p

def validate(a):
    assert re.fullmatch(r'actividad_[0-9]{3,}', a['id']), 'ID inválido'
    assert isinstance(a['version'], int) and a['version'] > 0
    assert a['schema'] == 1
    assert a.get('motor_minimo', 1) <= 1, 'Actualiza el motor del juego'
    for k in ('titulo','final'):
        assert all(isinstance(a[k][l], str) for l in ('es','eu'))
    assert isinstance(a['pasos'], list) and a['pasos']
    for name, content in a['archivos'].items():
        safe(Path('/tmp/escenario-validacion'), name)
        assert all(isinstance(content[l],str) for l in ('es','eu'))
    for d in a.get('carpetas',[]): safe(Path('/tmp/escenario-validacion'), d)
    for step in a['pasos']:
        for l in ('es','eu'):
            assert isinstance(step['texto'][l],str)
            assert isinstance(step['pistas'][l],list) and step['pistas'][l]
        assert step['pruebas']
        for test in step['pruebas']:
            assert test['tipo'] in ('respuesta','carpeta','contenido','ausente','vacio','respuesta_sistema','salida','entorno','texto','reentrada')
            if test['tipo']=='respuesta':
                assert all(isinstance(test['pregunta'][l],str) for l in ('es','eu'))
                assert all(isinstance(test['respuestas'][l],list) and test['respuestas'][l] for l in ('es','eu'))
            elif test['tipo'] in ('respuesta_sistema','salida'):
                from retos import QUERIES
                assert test['consulta'] in QUERIES
                if test['tipo']=='salida': safe(Path('/tmp/escenario-validacion'),test['ruta'])
                else: assert all(isinstance(test['pregunta'][l],str) for l in ('es','eu'))
            elif test['tipo']=='entorno':
                assert test['nombre'] in ('PROMPT', 'PATH')
                assert isinstance(test['valor'], str)
            elif test['tipo']=='texto':
                safe(Path('/tmp/escenario-validacion'), test['ruta'])
                assert test['lineas'] and all(isinstance(v,str) for v in test['lineas'])
            elif test['tipo']=='reentrada':
                pass
            else:
                safe(Path('/tmp/escenario-validacion'), test['ruta'])
                if test['tipo']=='contenido':
                    assert test['origen'] in a['archivos']
    return a

def available():
    found=[]
    ids=set()
    for p in sorted(CATALOG.glob('*.json')):
        try:
            a=validate(read(p))
            if a['id'] in ids: raise ValueError('ID duplicado')
            ids.add(a['id']); found.append(a)
        except (ValueError, KeyError, AssertionError, TypeError) as e:
            print(f'{p.name}: {e}')
    return sorted(found,key=lambda a:a['id'])

def folder(aid):
    if not re.fullmatch(r'actividad_[0-9]{3,}', aid): raise ValueError('ID inválido')
    p=DATA/aid
    if p.is_symlink(): raise ValueError('Directorio de datos enlazado')
    return p

def load(aid):
    d=folder(aid)
    return read(d/'actividad.json'), read(d/'estado.json'), d/'escenario'

def start(a):
    d=folder(a['id'])
    if (d/'estado.json').exists(): return load(a['id'])
    if (d/'escenario').exists():
        raise ValueError('Escenario sin estado: recupera tus archivos antes de continuar.')
    d.mkdir(parents=True, exist_ok=True)
    w=d/'escenario'; w.mkdir()
    for name in a.get('carpetas',[]): safe(w,name).mkdir(parents=True,exist_ok=True)
    language=lang()
    for name, content in a['archivos'].items():
        p=safe(w,name); p.parent.mkdir(parents=True,exist_ok=True)
        p.write_bytes(loc(content,language).replace('\r\n','\n').replace('\n','\r\n').encode('utf-8'))
    write(d/'actividad.json',a)
    write(d/'estado.json',{'paso':0,'pistas':{},'idioma_escenario':language,'cwd':'.'})
    return load(a['id'])

def show(aid, fresh=False, notice=None):
    a,s,w=load(aid)
    if fresh: ui.clear()
    if notice: print(ui.color(notice, "success"))
    print('\n'+ui.color(loc(a['titulo']), 'title'))
    if a.get('introduccion'): print(loc(a['introduccion']))
    if a.get('version',1)<2:
        print(tr('Hay una edición nueva de dinosaurios. REINICIAR carga esa edición y borra solo el trabajo de esta actividad.', 'Dinosauroen edizio berria dago. REINICIAR komandoak edizio hori kargatu eta jarduera honetako lana bakarrik ezabatzen du.'))
    print(ui.color(tr('Raíz del escenario: ','Eszenatokiaren erroa: ')+str(w), 'muted'))
    if s['paso']>=len(a['pasos']):
        print(ui.highlight(loc(a['final'])))
        print(ui.color(tr('Actividad completada. MENU para volver.','Jarduera osatuta. MENU itzultzeko.'), 'success'))
        return
    print(ui.color(tr('Paso','Urratsa')+f" {s['paso']+1}/{len(a['pasos'])}", "title"))
    print(ui.highlight(loc(a['pasos'][s['paso']]['texto']).replace('{escenario}',str(w))))
    print('\n'+ui.highlight('PISTA · COMPROBAR · AYUDA · REINICIAR · MENU'))

def check_test(test,a,s,w,answer=input):
    kind=test['tipo']
    if kind not in ('respuesta','carpeta','contenido','ausente','vacio'):
        from retos import check as check_unit
        return check_unit(test,a,s,w,answer,loc,safe)
    if kind=='respuesta':
        value=answer(ui.color(loc(test['pregunta']), 'command')+' ').strip().casefold()
        acceptable=loc(test['respuestas'],s['idioma_escenario'])
        return value in [x.replace('{escenario}',str(w)).casefold() for x in acceptable]
    p=safe(w,test['ruta'])
    if p.is_symlink() or (hasattr(p, 'is_junction') and p.is_junction()): return False
    if kind=='carpeta': return p.is_dir()
    if kind=='ausente': return not p.exists()
    if kind=='vacio': return p.is_file() and p.stat().st_size==0
    if kind=='contenido':
        expected=loc(a['archivos'][test['origen']],s['idioma_escenario']).replace('\r\n','\n').encode('utf-8')
        return p.is_file() and p.read_bytes().replace(b'\r\n',b'\n')==expected
    return False

def check(aid):
    a,s,w=load(aid)
    if s['paso']>=len(a['pasos']): show(aid); return
    step=a['pasos'][s['paso']]
    for test in step['pruebas']:
        if not check_test(test,a,s,w):
            print(ui.color(loc(test.get('error',{'es':'Todavía no está resuelto. Revisa el objetivo o escribe PISTA.','eu':'Oraindik ez dago ebatzita. Berrikusi helburua edo idatzi PISTA.'})), 'error'))
            return
    s['paso']+=1
    s['sesion_paso']=os.environ.get('LA_SESSION_ID','')
    write(folder(aid)/'estado.json',s)
    show(aid, fresh=True, notice=tr('¡Correcto! Progreso guardado.','Zuzen! Aurrerapena gordeta.'))

def hint(aid):
    a,s,w=load(aid)
    if s['paso']>=len(a['pasos']): show(aid); return
    hints=loc(a['pasos'][s['paso']]['pistas'])
    key=str(s['paso']); n=min(s['pistas'].get(key,0),len(hints)-1)
    print(ui.color(f'PISTA {n+1}/{len(hints)}: ', 'hint')+ui.highlight(hints[n].replace('{escenario}',str(w))))
    s['pistas'][key]=n+1; write(folder(aid)/'estado.json',s)

def reset(aid):
    a,s,w=load(aid)
    print(tr('Se borrará el trabajo de ESTA actividad. Las demás se conservan.','Jarduera HONETAKO lana ezabatuko da. Besteak mantenduko dira.'))
    if input(tr('Escribe REINICIAR para confirmar: ','Idatzi REINICIAR berresteko: ')).strip()!='REINICIAR':
        print(tr('Cancelado.','Bertan behera.')); return
    # Validate replacement before deleting anything. Never follow a workspace symlink.
    replacement=next((x for x in available() if x['id']==aid),a)
    validate(replacement)
    if w.is_symlink() or (hasattr(w, 'is_junction') and w.is_junction()): raise ValueError('Escenario enlazado: reinicio rechazado.')
    if w.exists(): shutil.rmtree(w)
    (folder(aid)/'estado.json').unlink()
    for name in ('alias_guardados.sh','alias_comprobacion.txt','historial_comprobacion.txt'):
        (folder(aid)/name).unlink(missing_ok=True)
    start(replacement); show(aid, fresh=True)

def remember(aid, cwd):
    a,s,w=load(aid)
    try: rel=Path(cwd).resolve().relative_to(w.resolve())
    except ValueError: return
    if Path(cwd).is_dir():
        s['cwd']=rel.as_posix(); write(folder(aid)/'estado.json',s)

def cwd(aid):
    a,s,w=load(aid)
    p=w if s.get('cwd','.')=='.' else safe(w,s['cwd'])
    return p if p.is_dir() else w

def help_text():
    print(ui.highlight(tr(
"""CÓMO SE JUEGA
Lee el objetivo, utiliza CMD real y escribe COMPROBAR.
PISTA: ayuda progresiva. AYUDA: instrucciones y objetivo.
REINICIAR: reconstruye SOLO la actividad actual, previa confirmación.
MENU: selector. SALIR: cierra el juego. EXIT: vuelve al menú.
ACTUALIZAR: nuevas actividades. La actualización completa se hace fuera del juego.
Los archivos y los pasos superados se conservan.
Los comandos se muestran en MAYÚSCULAS, pero CMD no distingue su caja.
Usa rutas entre comillas si contienen espacios. No necesitas ser administrador.
Estás en CMD real, con tus permisos; la carpeta del juego no es un aislamiento.
Las actividades de esta unidad no requieren crear archivos ni scripts.
No cambies PATH eliminando su contenido: perderías el acceso a los comandos.
Los colores y el título son de sesión. Las teclas Tab/flechas no se comprueban.
""",
"""NOLA JOKATU
Irakurri helburua, erabili benetako CMD eta idatzi COMPROBAR.
PISTA: laguntza mailakatua. AYUDA: argibideak eta helburua.
REINICIAR: uneko jarduera BAKARRIK berreraiki, berretsi ondoren.
MENU: hautatzailea. SALIR: jokoa itxi. EXIT: menura itzuli.
ACTUALIZAR: jarduera berriak. Programa osoa jokotik kanpo eguneratzen da.
Fitxategiak eta gainditutako urratsak gordetzen dira.
CMDk ez ditu letra larriak eta xeheak bereizten.
Jarri komatxoak zuriuneak dituzten bideetan. Ez da administratzailerik behar.
Benetako CMD da, zure baimenekin; jokoaren karpeta ez da isolamendua.
Unitate honetako jarduerek ez dute fitxategirik edo scriptik sortzea eskatzen.
Ez ezabatu PATH aldagaiko edukia: komandoetarako sarbidea galduko zenuke.
Koloreak eta izenburua saiokoak dira. Tab/gezi teklak ez dira egiaztatzen.
""")))


def fetch(url):
    if not url.startswith('https://raw.githubusercontent.com/'):
        raise ValueError('Solo URLs HTTPS de raw.githubusercontent.com')
    with urllib.request.urlopen(url,timeout=15) as r:
        if not r.geturl().startswith('https://raw.githubusercontent.com/'):
            raise ValueError('Redirección no permitida')
        data=r.read(2_000_001)
        if len(data)>2_000_000: raise ValueError('Archivo demasiado grande')
        return data

def update():
    cfg=read(ROOT/'config.json'); base=cfg.get('url_base','').rstrip('/')
    if not base:
        print(tr('Falta configurar url_base en config.json. Consulta README.md. Puedes seguir jugando sin conexión.','Konfiguratu url_base config.json fitxategian. Ikusi README.md. Konexiorik gabe jokatzen jarrai dezakezu.')); return
    try:
        manifest=json.loads(fetch(base+'/catalogo.json'))
        assert manifest['schema']==1
        pending=[]; ids=set()
        for entry in manifest['actividades']:
            name=entry['archivo']
            assert re.fullmatch(r'actividad_[0-9]{3,}\.json',name)
            raw=fetch(base+'/actividades/'+name)
            assert hashlib.sha256(raw).hexdigest()==entry['sha256'], 'SHA-256'
            a=validate(json.loads(raw))
            assert name==a['id']+'.json' and a['id'] not in ids
            ids.add(a['id'])
            dest=CATALOG/name
            if dest.exists() and read(dest)['version']>=a['version']: continue
            pending.append((dest,a))
        # Download and validate every candidate before publishing; states are snapshots.
        for dest,a in pending: write(dest,a)
        print(tr('Actividades incorporadas/actualizadas: ','Gehitutako/eguneratutako jarduerak: ')+str(len(pending)))
        print(tr('Las actividades iniciadas conservan su versión hasta REINICIAR.','Hasitako jarduerek beren bertsioa mantentzen dute REINICIAR egin arte.'))
    except (OSError,ValueError,KeyError,AssertionError,TypeError) as e:
        print(tr('No se pudo actualizar. Puedes seguir jugando. Detalle: ','Ezin izan da eguneratu. Jokatzen jarrai dezakezu. Xehetasuna: ')+str(e))

def main():
    action=sys.argv[1]; aid=os.environ.get('LA_ID')
    if aid and action not in ('path','remember'): remember(aid,os.getcwd())
    if action=='check': check(aid)
    elif action=='hint': hint(aid)
    elif action=='show': show(aid, fresh=True)
    elif action=='reset':
        os.chdir(ROOT)
        reset(aid)
    elif action=='help': ui.clear(); help_text(); show(aid)
    elif action=='update': update()
    elif action=='remember': remember(aid,sys.argv[2])
    elif action=='path': print(cwd(aid))

if __name__=='__main__':
    try: main()
    except (KeyboardInterrupt,EOFError): print('\n'+tr('Cancelado.','Bertan behera.'))
    except (OSError,ValueError,KeyError,AssertionError) as e:
        print(tr('Error: ','Errorea: ')+str(e),file=sys.stderr); sys.exit(1)
