import copy,io,json,os,shutil,subprocess,sys,tempfile,unittest,zipfile
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import motor as m,retos,actualizar
ROOT=m.ROOT
class EngineTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.data=Path(self.temp.name)/'datos'
        self.p=patch.object(m,'DATA',self.data);self.p.start();self.addCleanup(self.p.stop)
        self.env=patch.dict(os.environ,{'LA_SESSION_ID':'session-A','PROMPT':'[IZAR] $P$G'});self.env.start();self.addCleanup(self.env.stop)
    def prepare_test(self,t,a,s,w):
        k=t['tipo']
        if k in ('respuesta','respuesta_sistema'):return
        if k=='entorno':os.environ[t['nombre']]=t['valor'];return
        if k=='reentrada':s['sesion_paso']='old-session';return
        p=m.safe(w,t['ruta']);p.parent.mkdir(parents=True,exist_ok=True)
        if k=='carpeta':p.mkdir(exist_ok=True)
        elif k=='ausente':
            if p.is_dir():shutil.rmtree(p)
            else:p.unlink(missing_ok=True)
        elif k=='vacio':p.write_bytes(b'')
        elif k=='contenido':p.write_bytes(m.loc(a['archivos'][t['origen']],s['idioma_escenario']).replace('\n','\r\n').encode())
        elif k=='texto':p.write_text('\n'.join(t['lineas']),encoding='utf-8')
        elif k=='salida':p.write_text('SALIDA REAL',encoding='utf-8')
    def test_every_stage_both_languages(self):
        for language in ('es','eu'):
            shutil.rmtree(self.data,ignore_errors=True)
            m.write(self.data/'preferencias.json',{'idioma':language})
            acts=m.available();self.assertEqual(13,len(acts))
            for a in acts:
                with self.subTest(language=language,activity=a['id']):
                    saved,s,w=m.start(a)
                    for step in a['pasos']:
                        for t in step['pruebas']:
                            self.prepare_test(t,a,s,w)
                            response=m.loc(t['respuestas'],language)[0].replace('{escenario}',str(w)) if t['tipo']=='respuesta' else 'SALIDA REAL'
                            with patch.object(retos,'query',return_value='SALIDA REAL'):
                                self.assertTrue(m.check_test(t,a,s,w,lambda _:response),(a['id'],t))
    def test_wrong_answer_does_not_advance(self):
        a=m.available()[0];m.start(a)
        with patch('builtins.input',return_value='incorrecto'),redirect_stdout(io.StringIO()):
            # check_test's bound default input is replaced explicitly for this behavior test.
            with patch.object(m,'check_test',return_value=False):m.check(a['id'])
        self.assertEqual(0,m.load(a['id'])[1]['paso'])
    def test_check_saves_progress(self):
        a=m.available()[0];m.start(a)
        with patch.object(m,'check_test',return_value=True),redirect_stdout(io.StringIO()):m.check(a['id'])
        self.assertEqual(1,m.load(a['id'])[1]['paso'])
    def test_hints_progress(self):
        a=m.available()[0];m.start(a)
        with redirect_stdout(io.StringIO()):m.hint(a['id']);m.hint(a['id']);m.hint(a['id'])
        self.assertEqual(2,m.load(a['id'])[1]['pistas']['0'])
    def test_snapshots_preserved(self):
        a=m.available()[0];m.start(a);new=copy.deepcopy(a);new['version']=3
        m.start(new);self.assertEqual(2,m.load(a['id'])[0]['version'])
    def test_restart_isolated(self):
        a,b=m.available()[:2];m.start(a);m.start(b)
        m.safe(m.load(a['id'])[2],'alumno.txt').write_text('a')
        other=m.safe(m.load(b['id'])[2],'alumno.txt');other.write_text('b')
        with patch('builtins.input',return_value='REINICIAR'),redirect_stdout(io.StringIO()):m.reset(a['id'])
        self.assertFalse((m.load(a['id'])[2]/'alumno.txt').exists());self.assertEqual('b',other.read_text())
    def test_cancel_restart(self):
        a=m.available()[0];m.start(a);p=m.load(a['id'])[2]/'alumno.txt';p.write_text('x')
        with patch('builtins.input',return_value='NO'),redirect_stdout(io.StringIO()):m.reset(a['id'])
        self.assertEqual('x',p.read_text())
    def test_damaged_copy_rejected(self):
        a=copy.deepcopy(m.available()[2]);a['archivos']={'documentos/mapa.txt':{'es':'Original','eu':'Jatorrizkoa'}};a,s,w=m.start(a)
        p=w/'copia.txt';p.write_text('falso')
        self.assertFalse(m.check_test({'tipo':'contenido','ruta':'copia.txt','origen':'documentos/mapa.txt'},a,s,w))
    def test_empty_file_rejected_if_nonempty(self):
        a=m.available()[0];a,s,w=m.start(a);(w/'x').write_text('x')
        self.assertFalse(m.check_test({'tipo':'vacio','ruta':'x'},a,s,w))
    def test_unsafe_paths(self):
        for name in ('../fuera','C:/fuera','C:fuera','\\\\servidor\\x','x:ads','CON.txt','x.','/tmp/x'):
            with self.subTest(name=name),self.assertRaises(ValueError):m.safe(self.data,name)
    def test_reentry(self):
        a=m.available()[0];a,s,w=m.start(a);s['sesion_paso']='session-A'
        t={'tipo':'reentrada'}
        self.assertFalse(m.check_test(t,a,s,w))
        with patch.dict(os.environ,{'LA_SESSION_ID':'session-B'}):self.assertTrue(m.check_test(t,a,s,w))
    def test_script_not_executed(self):
        a=m.available()[0];a,s,w=m.start(a);(w/'x.bat').write_text('@echo off\necho LISTO')
        with patch.object(subprocess,'run',side_effect=AssertionError('No debe ejecutarse')):
            self.assertTrue(m.check_test({'tipo':'texto','ruta':'x.bat','lineas':['@echo off','echo LISTO']},a,s,w))
    def test_encoding(self):
        p=Path(self.temp.name)/'salida.txt'
        for encoding in ('utf-8','utf-16','utf-16-le','cp850'):
            p.write_bytes('Información de versión\r\n'.encode(encoding))
            self.assertEqual('Información de versión\r\n',retos.read_text(p))
    def test_curriculum_and_theme(self):
        allowed=set('CHKDSK CLS CMD COLOR DATE EXIT HELP LABEL PATH PROMPT SHUTDOWN SYSTEMINFO START TIME TITLE VER VOL'.split())
        acts=m.available();seen=set()
        for a in acts:
            self.assertEqual(2,a['version'])
            self.assertFalse(a['archivos'])
            self.assertIn('introduccion',a)
            seen.update(a['comandos_temario'])
            for step in a['pasos']:
                for line in step['solucion_docente'].splitlines():
                    if not line.strip():continue
                    self.assertIn(line.split()[0].upper(),allowed|{'COMPROBAR','REM'})
                for t in step['pruebas']:
                    self.assertIn(t['tipo'],('respuesta','respuesta_sistema','entorno','reentrada'))
        self.assertEqual(allowed,seen)
        self.assertEqual(17,len(acts[-1]['pasos']))
    def test_catalog_hashes(self):
        import hashlib
        for e in m.read(ROOT/'catalogo.json')['actividades']:
            self.assertEqual(e['sha256'],hashlib.sha256((m.CATALOG/e['archivo']).read_bytes()).hexdigest())
class UpdateTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.r=Path(self.tmp.name)
    def test_preserves_data_config_and_backup(self):
        old=self.r/'windowsaventura';new=self.r/'stage'
        old.mkdir();new.mkdir();(old/'jugar.bat').write_text('old');(new/'jugar.bat').write_text('new')
        (old/'datos').mkdir();(old/'datos'/'script.bat').write_text('student')
        (old/'config.json').write_text('oldconfig')
        backup=actualizar.install(new,old)
        self.assertEqual('student',(old/'datos'/'script.bat').read_text())
        self.assertEqual('oldconfig',(old/'config.json').read_text())
        self.assertEqual('old',(backup/'jugar.bat').read_text())
    def test_rejects_unrelated_folder(self):
        old=self.r/'other';old.mkdir();new=self.r/'new';new.mkdir()
        with self.assertRaises(ValueError):actualizar.install(new,old)
    def test_zip_traversal(self):
        for name in ('../escape','root/C:stream','root/CON.txt','root/back\\name'):
            p=self.r/'evil.zip'
            with zipfile.ZipFile(p,'w') as z:z.writestr(name,'x')
            with zipfile.ZipFile(p) as z,self.assertRaises(ValueError):list(actualizar.safe_entries(z))
    def test_zip_unpack(self):
        p=self.r/'normal.zip'
        with zipfile.ZipFile(p,'w') as z:
            for f in ROOT.rglob('*'):
                if f.is_file() and '__pycache__' not in f.parts and 'datos' not in f.parts:z.write(f,'windowsaventura-main/'+f.relative_to(ROOT).as_posix())
        src=actualizar.unpack(p,self.r/'unpacked')
        self.assertTrue((src/'jugar.bat').is_file())
@unittest.skipUnless(os.name=='nt','Necesita CMD real en Windows')
class WindowsIntegration(unittest.TestCase):
    def test_real_cmd_help_and_check(self):
        with tempfile.TemporaryDirectory(prefix='wa prueba ') as tmp:
            root=Path(tmp)/'juego';shutil.copytree(ROOT,root,ignore=shutil.ignore_patterns('datos','__pycache__'))
            env=os.environ.copy();env.update(PYTHONUTF8='1',PYTHONIOENCODING='utf-8',LA_ROOT=str(root),LA_ID='actividad_001',LA_SESSION_ID='test',LA_PYTHON=sys.executable)
            env['PATH']=str(root/'comandos')+os.pathsep+env['PATH']
            setup='import motor as m; m.write(m.DATA/"preferencias.json",{"idioma":"es"}); m.start(m.available()[0])'
            subprocess.run([sys.executable,'-c',setup],cwd=root,env=env,check=True)
            work=root/'datos'/'actividad_001'/'escenario';env['LA_SCENARIO']=str(work)
            script=work/'test-driver.bat'
            script.write_bytes(('@echo off\r\ncall "%LA_ROOT%\\terminal.bat"\r\nhelp\r\ncall COMPROBAR\r\n').encode('utf-8'))
            result=subprocess.run(f'"{env["COMSPEC"]}" /d /v:off /s /c ""{script}""',cwd=work,env=env,input=b'HELP\r\n',capture_output=True,timeout=45)
            state=json.loads((work.parent/'estado.json').read_text(encoding='utf-8'))
            self.assertEqual(1,state['paso'],result.stdout.decode('utf-8',errors='replace')+result.stderr.decode('utf-8',errors='replace'))
if __name__=='__main__':unittest.main(verbosity=2)
