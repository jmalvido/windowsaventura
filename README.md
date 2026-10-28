# WindowsAventura

Juego educativo para practicar CMD y archivos .bat en una máquina virtual Windows.
Usa CMD real. Python solo gestiona menú, actividades y progreso. No usa PowerShell,
Bash ni WSL. Incluye 12 juegos independientes y un extra de 30 definiciones,
en castellano y euskera.

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
Dentro de un .bat usa CALL COMPROBAR o CALL PISTA para regresar al script.
En la terminal interactiva basta con COMPROBAR.

Los archivos permanecen en datos\actividad_NNN\escenario. Los pasos se guardan tras
cada acierto. MENU recuerda la carpeta; EXIT conserva archivos y pasos pero no registra
el último cambio de carpeta. El título, color y prompt son de sesión: si una etapa
comprueba el prompt, vuelve a establecerlo al entrar.

Las actividades empezadas conservan su versión y el idioma de sus archivos hasta
REINICIAR. Cambiar el idioma no sobrescribe el trabajo. La carpeta del escenario
organiza la práctica, pero no limita los permisos de CMD.

## Juegos

| Nº | Actividad | Contenido |
|---|---|---|
| 1 | Bienvenido a Windows 1 | CD, DIR, TYPE, rutas |
| 2 | Bienvenido a Windows 2 | HELP, /?, CLS, VER, DATE, TIME, Tab |
| 3 | Bienvenido a Windows 3 | MD, COPY, REN, MOVE, archivo vacío |
| 4 | Encuentra el virus | Investigación y cuarentena de texto |
| 5 | Tu puesto de mando | TITLE, COLOR, PROMPT |
| 6 | El inventario del equipo | SYSTEMINFO, consultas e informes |
| 7 | La unidad bajo examen | VOL, LABEL, CHKDSK |
| 8 | Ventanas y rutas de búsqueda | PATH, CMD, START, EXIT |
| 9 | El apagado planificado | SHUTDOWN, cancelación, accesos directos |
| 10 | Tu primer archivo bat | ECHO, CALL, edición y ejecución |
| 11 | El relevo del técnico | Rutas con espacios e informes |
| 12 | Operación IZAR | Misión final de 12 etapas |
| 13 | Extra | 30 definiciones |

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

18 pruebas de lógica han pasado en Linux, incluidas las condiciones de todas las etapas
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
