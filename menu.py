"""Menú libre. Cada actividad abre un CMD interactivo real."""
import os,sys,subprocess,uuid
import motor as m
import interfaz as ui
def choose_language():
    while True:
        v=input('1. Castellano / 2. Euskera > ').strip()
        if v in ('1','2'):
            m.write(m.DATA/'preferencias.json',{'idioma':'es' if v=='1' else 'eu'});return
def main():
    if os.name!='nt':
        print('WindowsAventura necesita Windows y CMD.');return
    from actualizar import lock_install
    m.DATA.mkdir(exist_ok=True)
    with lock_install(m.ROOT):
        if not (m.DATA/'preferencias.json').exists():choose_language()
        while True:
            ui.clear()
            print(ui.color('WINDOWSAVENTURA 0.2 | PALEO ISLA | CMD','title'))
            acts=m.available()
            for i,a in enumerate(acts,1):
                status=m.tr('Sin empezar','Hasi gabe')
                if (m.folder(a['id'])/'estado.json').exists():
                    old,s,w=m.load(a['id'])
                    status=m.tr('Completada','Osatuta') if s['paso']>=len(old['pasos']) else m.tr('En curso','Abian')+f" {s['paso']}/{len(old['pasos'])}"
                print(f"{i:2}. {m.loc(a['titulo'])} [{status}]")
            print(ui.highlight('ACTUALIZAR · IDIOMA · AYUDA · SALIR'))
            c=input('> ').strip().upper()
            if c=='SALIR':return
            if c=='IDIOMA':choose_language();continue
            if c in ('AYUDA','ACTUALIZAR'):
                m.help_text() if c=='AYUDA' else m.update()
                ui.pause(m.tr('Intro para continuar.','Sartu jarraitzeko.'));continue
            if not c.isdigit() or not 1<=int(c)<=len(acts):continue
            a=acts[int(c)-1];m.start(a)
            env=os.environ.copy()
            env.update(LA_ROOT=str(m.ROOT),LA_ID=a['id'],LA_SESSION_ID=uuid.uuid4().hex,LA_PYTHON=sys.executable,
                       LA_SCENARIO=str(m.load(a['id'])[2]),PYTHONUTF8='1',PYTHONIOENCODING='utf-8')
            env['PATH']=str(m.ROOT/'comandos')+os.pathsep+env.get('PATH','')
            # /d disables registry AutoRun; /v:off preserves exclamation marks in paths.
            flag=m.DATA/'salir.flag';flag.unlink(missing_ok=True)
            subprocess.run(f'"{os.environ["COMSPEC"]}" /d /v:off /s /k ""{m.ROOT / "terminal.bat"}""',
                           cwd=m.cwd(a['id']),env=env)
            if flag.exists():flag.unlink();return
if __name__=='__main__':
    try:main()
    except (KeyboardInterrupt,EOFError):print('\nAgur / Hasta pronto.')
    except (OSError,ValueError,KeyError,AssertionError,RuntimeError) as e:print('Error / Errorea:',e);sys.exit(1)
