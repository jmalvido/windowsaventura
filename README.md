# WindowsAventura

Paleo Isla es una aventura de dinosaurios para practicar CMD real en Windows.
Python gestiona menú y progreso. Los .bat del paquete solo arrancan y actualizan
el programa: no se pide crearlos ni programarlos en las actividades.

Incluye 12 juegos independientes y un extra de 17 definiciones, en castellano y euskera.
Los ejercicios se ciñen a los 17 comandos del material aportado. No requieren
administración de archivos, redirecciones ni comandos de otras unidades.
La historia y las instrucciones aparecen directamente en la pantalla del juego.

## Descargar y jugar

1. Instala Python 3.10 o posterior desde https://www.python.org/downloads/windows/.
   Activa Add python.exe to PATH y abre un CMD nuevo.
2. Descomprime el paquete y coloca windowsaventura en tu carpeta de usuario.
   Debe existir %USERPROFILE%\windowsaventura\jugar.bat.
3. Abre Símbolo del sistema con Windows+R → cmd y ejecuta:

```bat
cd /d "%USERPROFILE%\windowsaventura"
jugar.bat
```

También puedes abrir jugar.bat con doble clic. No ejecutes el juego como administrador.
El lanzador busca py -3 y, si no está disponible, python. No requiere paquetes pip.

## Cómo jugar

Elige el idioma y cualquier actividad. Lee el objetivo, trabaja en CMD y escribe COMPROBAR.

| Comando | Función |
|---|---|
| COMPROBAR | Revisa archivos, entorno o respuestas; avanza y guarda |
| PISTA | Orientación y después solución más concreta |
| AYUDA | Reglas y objetivo actual |
| REINICIAR | Reconstruye solo esta actividad, previa confirmación |
| MENU | Vuelve al selector conservando trabajo y carpeta actual |
| SALIR | Cierra el juego |
| EXIT | Sale del CMD de la actividad y vuelve al menú |
| ACTUALIZAR | Descarga actividades del repositorio configurado |
| IDIOMA | Cambia el idioma desde el menú |

Los comandos del juego se muestran en mayúsculas, pero CMD no distingue su caja.
Escribe COMPROBAR directamente en la terminal interactiva.

Los archivos permanecen en datos\actividad_NNN\escenario. Los pasos se guardan tras
cada acierto. MENU recuerda la carpeta; EXIT conserva archivos y pasos pero no registra
el último cambio de carpeta. El título, color y prompt son de sesión: si una etapa
comprueba el prompt, vuelve a establecerlo al entrar.

Las actividades empezadas conservan su versión y el idioma de sus archivos hasta
REINICIAR. Cambiar el idioma no sobrescribe el trabajo. La carpeta del escenario
organiza la práctica, pero no limita los permisos de CMD.

## Juegos

| Nº | Misión | Comandos |
|---|---|---|
| 1 | Bienvenido a Paleo Isla — La consola del visitante | HELP, COLOR, CLS |
| 2 | Bienvenido a Paleo Isla — El reloj de la expedición | VER, DATE, TIME |
| 3 | Bienvenido a Paleo Isla — Tu puesto de guardia | TITLE, COLOR, PROMPT |
| 4 | La ficha del laboratorio de fósiles | SYSTEMINFO, VER, HELP |
| 5 | El turno de las incubadoras | DATE, TIME, CLS |
| 6 | El archivo de huellas | VOL, LABEL |
| 7 | El disco de las cámaras de los estegosaurios | CHKDSK, HELP |
| 8 | Las rutas de la estación de rastreo | PATH, CMD, VER |
| 9 | Una segunda torre de observación | START, CMD, VER, EXIT |
| 10 | El cierre del centro de visitantes | SHUTDOWN |
| 11 | Los accesos del puesto de los velociraptores | CMD, EXIT, SHUTDOWN |
| 12 | La gran reapertura de Paleo Isla | HELP, CLS, VER, SYSTEMINFO, DATE, TIME, TITLE, COLOR, PROMPT, PATH, VOL, LABEL, CHKDSK, START, CMD, EXIT, SHUTDOWN |
| 13 | Extra — El examen de los guardas del parque | 17 definiciones del temario |

Las órdenes de apagado y cambio de etiqueta se responden como texto. El programa
nunca las ejecuta automáticamente. Accesos directos, iconos y anclaje se revisan con
el profesor. CHKDSK real con elevación se hace aparte. Véase docs/PRACTICAS_SUPERVISADAS.md.

## Publicar y actualizar

Proyecto independiente de LinuxAventura. Repositorio propuesto: jmalvido/windowsaventura.
Este paquete no crea ni publica ese repositorio.

Crea el repositorio con rama main y sube el contenido de esta carpeta. No subas datos,
__pycache__ ni copias de alumnos. Después pon en config.json:

```json
{"url_base": "https://raw.githubusercontent.com/jmalvido/windowsaventura/main"}
```

Si eliges otro nombre, cambia también WA_REPO en actualizar_windowsaventura.bat.
Tras añadir o modificar actividades, aumenta version y ejecuta desde CMD:

```bat
py -3 publicar_catalogo.py
```

Sube el JSON y catalogo.json. El menú descubre las actividades automáticamente.

### Primera instalación desde el repositorio publicado

Con Python instalado, ejecuta en CMD:

```bat
cd /d "%USERPROFILE%"
curl.exe -fL "https://raw.githubusercontent.com/jmalvido/windowsaventura/main/actualizar_windowsaventura.bat" -o actualizar_windowsaventura.bat
actualizar_windowsaventura.bat
```

El instalador usa curl.exe y Python para descargar y descomprimir el ZIP de main.
No requiere wget. Solo funcionará cuando publiques el nuevo repositorio.

### Versiones nuevas

Cierra el juego y los editores con archivos abiertos en su carpeta. Ejecuta la copia
del actualizador que está fuera de la carpeta del juego:

```bat
cd /d "%USERPROFILE%"
actualizar_windowsaventura.bat
```

Conserva datos y la configuración local. Deja una copia de la versión anterior con
fecha y hora. Estas copias también contienen el trabajo del alumno y ocupan espacio.
Si falla la descarga o preparación, no sustituye la instalación. El bloqueo impide
actualizar mientras el menú siga abierto. ACTUALIZAR solo descarga actividades;
para actualizar el motor utiliza el archivo externo.

## Verificación

19 pruebas de lógica han pasado en Linux, incluidas las condiciones de todas las etapas
en ambos idiomas, guardado, reinicio aislado, codificaciones y actualización. Las consultas
del sistema están simuladas en esas pruebas; no equivalen a probar CMD real.

Hay una prueba adicional que solo se ejecuta en Windows:

```bat
cd /d "%USERPROFILE%\windowsaventura"
py -3 -m unittest discover -s tests -v
```

Usa una copia temporal y no modifica el progreso del alumno. Después sigue
 docs/PRUEBA_EN_WINDOWS.md para verificar la consola, los colores y las utilidades reales.
Guía de soluciones: docs/GUIA_PROFESOR.md.

## Pasar de la edición 0.1 a Paleo Isla 0.2

Actualiza el programa completo y las actividades. Conserva datos si quieres mantener
el progreso anterior. Una actividad ya iniciada conserva su versión antigua: entra en
ella y escribe REINICIAR para cargar el nuevo juego de dinosaurios. Se pedirá confirmación
porque se borran el progreso y el trabajo de esa actividad; las demás se conservan.
Las actividades sin empezar muestran directamente la edición nueva.

## Qué se comprueba

El motor compara respuestas, consultas del sistema, el PROMPT y la reentrada.
No demuestra que se haya ejecutado cada comando. El título, los colores, las teclas
y los accesos directos se revisan visualmente. Las consultas peligrosas se diseñan
como texto y se practican aparte con el profesor cuando corresponda.
