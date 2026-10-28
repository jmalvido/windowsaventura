# Guía docente de WindowsAventura 0.1

Enunciados, soluciones y comprobaciones. CMD real y archivos .bat. Esta guía está en castellano; ambas versiones del juego comparten objetivos.

## Cómo usar las soluciones

Las rutas relativas parten de la raíz del escenario, salvo indicación. En CMD puedes volver con CD /D "%LA_SCENARIO%". En un .bat usa CALL para invocar los comandos del juego. Las líneas con # son indicaciones editoriales: no las copies a CMD. Los comentarios reales de .bat usan REM. Cuando se muestra contenido de un script, escríbelo en el editor.

El corrector no ejecuta los scripts: inspecciona el contenido o su resultado. Las consultas dependen de la VM. La revisión de color, título, teclas y acciones gráficas es conceptual o del profesor.

## Mapa

| Nº | Juego | Etapas |
|---|---|---|
| 1 | Bienvenido a Windows 1 — Primeros pasos | 4 |
| 2 | Bienvenido a Windows 2 — Ayuda y consultas | 4 |
| 3 | Bienvenido a Windows 3 — Organiza archivos | 4 |
| 4 | Encuentra el virus | 4 |
| 5 | Tu puesto de mando | 4 |
| 6 | El inventario del equipo | 4 |
| 7 | La unidad bajo examen | 4 |
| 8 | Ventanas y rutas de búsqueda | 4 |
| 9 | El apagado planificado | 4 |
| 10 | Tu primer archivo bat | 4 |
| 11 | El relevo del técnico | 4 |
| 12 | Operación IZAR — Misión final | 12 |
| 13 | Extra — Adivina el comando | 30 |

## Juego 1 Bienvenido a Windows 1 — Primeros pasos

Escenario: datos/actividad_001/escenario

### Situación inicial

Bienvenido a CMD. La clave es KAIXO. El segundo mensaje está en centro/entrada.txt.

### Etapa 1 de 4

**Enunciado**

Estás en CMD real. CD, sin argumentos, muestra la carpeta actual. Escribe CD y después COMPROBAR. No escribas el símbolo > del prompt.

**Desarrollo resuelto**

```bat
CD
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Ruta completa:»: `{escenario}`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 2 de 4

**Enunciado**

DIR lista archivos y carpetas. Ejecuta DIR y localiza el archivo de bienvenida.

**Desarrollo resuelto**

```bat
DIR
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Nombre del archivo de bienvenida:»: `LEEME.txt`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 3 de 4

**Enunciado**

TYPE muestra el contenido. Ejecuta TYPE LEEME.txt y lee la clave.

**Desarrollo resuelto**

```bat
TYPE LEEME.txt
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Clave:»: `KAIXO`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 4 de 4

**Enunciado**

Entra con CD centro. Lista y lee entrada.txt. Después vuelve con CD .. antes de COMPROBAR. Las rutas Windows usan la barra invertida.

**Desarrollo resuelto**

```bat
CD centro
DIR
TYPE entrada.txt
CD ..
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Responsable:»: `ALEX`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.


## Juego 2 Bienvenido a Windows 2 — Ayuda y consultas

Escenario: datos/actividad_002/escenario

### Situación inicial

Bienvenido al centro IZAR. Lee las instrucciones y usa COMPROBAR al terminar cada paso.

### Etapa 1 de 4

**Enunciado**

HELP muestra la ayuda de comandos. Ejecuta HELP y después HELP DIR. ¿Qué símbolo acompaña a la barra para pedir ayuda con DIR /?

**Desarrollo resuelto**

```bat
HELP
HELP DIR
DIR /?
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Opción completa de ayuda:»: `/?`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 2 de 4

**Enunciado**

CLS limpia la pantalla. Ejecuta CLS y luego VER para consultar la versión de Windows. COMPROBAR pedirá la línea de versión completa.

**Desarrollo resuelto**

```bat
CLS
VER
COMPROBAR
```

**Qué comprueba**

- Compara la respuesta con la consulta real: version. Copia la salida de la VM, no un ejemplo.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 3 de 4

**Enunciado**

DATE /T y TIME /T muestran fecha y hora sin pedir cambios. Pruébalos. Usa flecha arriba para recuperar una orden.

**Desarrollo resuelto**

```bat
DATE /T
TIME /T
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Opción para consultar sin modificar:»: `/T`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 4 de 4

**Enunciado**

Tab completa nombres de archivos y carpetas. Prueba TYPE L y pulsa Tab para completar LEEME.txt; después pulsa Intro. La comprobación no registra la tecla, solo la respuesta.

**Desarrollo resuelto**

```bat
TYPE LEEME.txt
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Comando para leer un archivo:»: `TYPE`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.


## Juego 3 Bienvenido a Windows 3 — Organiza archivos

Escenario: datos/actividad_003/escenario

### Situación inicial

Bienvenido al centro IZAR. Lee las instrucciones y usa COMPROBAR al terminar cada paso.

### Etapa 1 de 4

**Enunciado**

Desde la raíz del escenario crea refugio y refugio\copias con MD. MD y MKDIR son equivalentes.

**Desarrollo resuelto**

```bat
MD refugio
MD refugio\copias
COMPROBAR
```

**Qué comprueba**

- Debe existir la carpeta `refugio/copias`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 2 de 4

**Enunciado**

COPY copia y conserva el original. Copia documentos\mapa.txt a refugio\copias.

**Desarrollo resuelto**

```bat
COPY documentos\mapa.txt refugio\copias\
COMPROBAR
```

**Qué comprueba**

- `refugio/copias/mapa.txt` debe conservar el contenido inicial de `documentos/mapa.txt`.
- `documentos/mapa.txt` debe conservar el contenido inicial de `documentos/mapa.txt`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 3 de 4

**Enunciado**

REN cambia el nombre. Renombra la copia a plano.txt; el segundo argumento de REN es el nombre nuevo, no otra carpeta.

**Desarrollo resuelto**

```bat
REN refugio\copias\mapa.txt plano.txt
COMPROBAR
```

**Qué comprueba**

- `refugio/copias/plano.txt` debe conservar el contenido inicial de `documentos/mapa.txt`.
- No debe existir `refugio/copias/mapa.txt`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 4 de 4

**Enunciado**

MOVE cambia la ubicación. Mueve plano.txt a refugio. Crea una señal vacía con TYPE NUL > refugio\listo.txt. > sobrescribe el destino; úsalo solo con esta señal.

**Desarrollo resuelto**

```bat
MOVE refugio\copias\plano.txt refugio\plano.txt
TYPE NUL > refugio\listo.txt
COMPROBAR
```

**Qué comprueba**

- `refugio/plano.txt` debe conservar el contenido inicial de `documentos/mapa.txt`.
- No debe existir `refugio/copias/plano.txt`.
- Debe ser un archivo de cero bytes `refugio/listo.txt`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.


## Juego 4 Encuentra el virus

Escenario: datos/actividad_004/escenario

### Situación inicial

Alerta IZAR. Empieza por informes\aviso.txt. Todos los archivos son texto inofensivo.

### Etapa 1 de 4

**Enunciado**

Lee el aviso y averigua el código de incidencia.

**Desarrollo resuelto**

```bat
TYPE LEEME.txt
TYPE informes\aviso.txt
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Código:»: `IZAR-17`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 2 de 4

**Enunciado**

Investiga almacen y lee los archivos. Identifica el sospechoso por su contenido.

**Desarrollo resuelto**

```bat
DIR almacen
TYPE almacen\actualizacion.txt
TYPE almacen\antivirus.txt
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Archivo sospechoso:»: `actualizacion.txt`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 3 de 4

**Enunciado**

Crea evidencias y copia el aviso. Crea cuarentena y mueve el sospechoso con el nombre sospechoso.txt. Conserva el otro paquete.

**Desarrollo resuelto**

```bat
MD evidencias
COPY informes\aviso.txt evidencias\
MD cuarentena
MOVE almacen\actualizacion.txt cuarentena\sospechoso.txt
COMPROBAR
```

**Qué comprueba**

- `evidencias/aviso.txt` debe conservar el contenido inicial de `informes/aviso.txt`.
- `cuarentena/sospechoso.txt` debe conservar el contenido inicial de `almacen/actualizacion.txt`.
- No debe existir `almacen/actualizacion.txt`.
- `almacen/antivirus.txt` debe conservar el contenido inicial de `almacen/antivirus.txt`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 4 de 4

**Enunciado**

Cierra la investigación creando evidencias\resuelto.txt vacío. Mover este texto es una simulación, no una desinfección real.

**Desarrollo resuelto**

```bat
TYPE NUL > evidencias\resuelto.txt
COMPROBAR
```

**Qué comprueba**

- Debe ser un archivo de cero bytes `evidencias/resuelto.txt`.
- `cuarentena/sospechoso.txt` debe conservar el contenido inicial de `almacen/actualizacion.txt`.
- `informes/aviso.txt` debe conservar el contenido inicial de `informes/aviso.txt`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.


## Juego 5 Tu puesto de mando

Escenario: datos/actividad_005/escenario

### Situación inicial

Bienvenido al centro IZAR. Lee las instrucciones y usa COMPROBAR al terminar cada paso.

### Etapa 1 de 4

**Enunciado**

Consulta HELP TITLE y cambia el título a Comandos. Observa la ventana o pestaña. La comprobación es conceptual; el profesor revisa el título.

**Desarrollo resuelto**

```bat
HELP TITLE
TITLE Comandos
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Orden usada:»: `TITLE Comandos`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 2 de 4

**Enunciado**

Consulta COLOR /?. Fondo azul y letras rojas: COLOR 14. El primer dígito es fondo; el segundo, texto. Después vuelve a COLOR 0B.

**Desarrollo resuelto**

```bat
COLOR /?
COLOR 14
COLOR 0B
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Código para fondo azul y texto rojo:»: `14`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 3 de 4

**Enunciado**

Prueba fondo blanco brillante con rojo brillante (COLOR FC) y después con rojo normal (COLOR F4). Consulta COLOR /? y vuelve a COLOR 0B.

**Desarrollo resuelto**

```bat
COLOR FC
COLOR F4
COLOR 0B
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Código con blanco brillante y rojo brillante:»: `FC`.
- Respuesta a «Código con blanco brillante y rojo normal:»: `F4`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 4 de 4

**Enunciado**

Personaliza el prompt con PROMPT [IZAR] $P$G. $P es la ruta y $G representa >. No escribas > literal en esta orden.

**Desarrollo resuelto**

```bat
PROMPT [IZAR] $P$G
COMPROBAR
```

**Qué comprueba**

- El entorno CMD debe tener PROMPT igual a `[IZAR] $P$G`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.


## Juego 6 El inventario del equipo

Escenario: datos/actividad_006/escenario

### Situación inicial

Bienvenido al centro IZAR. Lee las instrucciones y usa COMPROBAR al terminar cada paso.

### Etapa 1 de 4

**Enunciado**

Consulta VER y guarda la salida en version.txt usando >. Esta redirección reemplaza el contenido del archivo.

**Desarrollo resuelto**

```bat
VER > version.txt
TYPE version.txt
COMPROBAR
```

**Qué comprueba**

- `version.txt` debe contener la salida de la consulta version.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 2 de 4

**Enunciado**

Consulta DATE /T y TIME /T. COMPROBAR pedirá la fecha completa tal como aparece, incluido el día de la semana si lo muestra.

**Desarrollo resuelto**

```bat
DATE /T
TIME /T
COMPROBAR
```

**Qué comprueba**

- Compara la respuesta con la consulta real: fecha. Copia la salida de la VM, no un ejemplo.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 3 de 4

**Enunciado**

Consulta SYSTEMINFO /? y ejecuta SYSTEMINFO. Puede tardar. Localiza sistema operativo, memoria y nombre del equipo. Para copiar el nombre sin etiquetas puedes consultar ECHO %COMPUTERNAME%.

**Desarrollo resuelto**

```bat
SYSTEMINFO /?
SYSTEMINFO
ECHO %COMPUTERNAME%
COMPROBAR
```

**Qué comprueba**

- Compara la respuesta con la consulta real: equipo. Copia la salida de la VM, no un ejemplo.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 4 de 4

**Enunciado**

Prepara un pequeño informe con el nombre del equipo y conserva version.txt.

**Desarrollo resuelto**

```bat
ECHO %COMPUTERNAME% > equipo.txt
COMPROBAR
```

**Qué comprueba**

- `equipo.txt` debe contener la salida de la consulta equipo.
- `version.txt` debe contener la salida de la consulta version.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.


## Juego 7 La unidad bajo examen

Escenario: datos/actividad_007/escenario

### Situación inicial

Bienvenido al centro IZAR. Lee las instrucciones y usa COMPROBAR al terminar cada paso.

### Etapa 1 de 4

**Enunciado**

VOL consulta etiqueta y número de serie. Ejecuta VOL %SystemDrive% y guarda el resultado en volumen.txt. No cambies la etiqueta.

**Desarrollo resuelto**

```bat
VOL %SystemDrive% > volumen.txt
TYPE volumen.txt
COMPROBAR
```

**Qué comprueba**

- `volumen.txt` debe contener la salida de la consulta volumen.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 2 de 4

**Enunciado**

Consulta LABEL /?. No lo ejecutes para modificar el disco del sistema. ¿Qué orden asignaría APELLIDO a una unidad USB E: ya identificada? Contesta como texto; E: es solo un ejemplo.

**Desarrollo resuelto**

```bat
LABEL /?
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Orden de ejemplo, sin ejecutarla:»: `LABEL E: APELLIDO`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 3 de 4

**Enunciado**

Consulta CHKDSK /?. Sin /F ni /R informa sin pedir reparaciones. La ejecución real se hará aparte, en CMD como administrador con el profesor; el juego no necesita elevación.

**Desarrollo resuelto**

```bat
CHKDSK /?
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Orden para consultar C: sin solicitar reparación:»: `CHKDSK C:`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 4 de 4

**Enunciado**

Distingue etiqueta, número de serie y comprobación. ¿Qué opción de CHKDSK solicita reparar errores? No la ejecutes.

**Desarrollo resuelto**

```bat
HELP CHKDSK
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Opción de reparación:»: `/F`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.


## Juego 8 Ventanas y rutas de búsqueda

Escenario: datos/actividad_008/escenario

### Situación inicial

Bienvenido al centro IZAR. Lee las instrucciones y usa COMPROBAR al terminar cada paso.

### Etapa 1 de 4

**Enunciado**

PATH sin argumentos muestra dónde busca ejecutables CMD. Consúltalo sin sustituir su contenido.

**Desarrollo resuelto**

```bat
PATH
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Separador entre carpetas en PATH:»: `;`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 2 de 4

**Enunciado**

CMD /C ejecuta una orden y termina; CMD /K ejecuta y permanece abierto. Ejecuta CMD /C VER.

**Desarrollo resuelto**

```bat
CMD /C VER
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Opción que termina tras la orden:»: `/C`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 3 de 4

**Enunciado**

Prueba START "Practica" CMD /D /K VER. Se abre otra consola o pestaña. Ciérrala con EXIT y vuelve a la actividad original. El primer texto entre comillas de START es el título.

**Desarrollo resuelto**

```bat
START "Practica" CMD /D /K VER
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Qué representa Practica: escribe TITULO.»: `TITULO` / `TÍTULO`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 4 de 4

**Enunciado**

Para practicar EXIT en la consola principal, sal de esta actividad y vuelve a entrar desde el menú. Después escribe COMPROBAR.

**Desarrollo resuelto**

```bat
EXIT
# Volver a la actividad 8 / Itzuli 8. jarduerara
COMPROBAR
```

**Qué comprueba**

- Debe abrirse otra sesión después del paso anterior. MENU también sirve para la comprobación; EXIT es la práctica solicitada.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.


## Juego 9 El apagado planificado

Escenario: datos/actividad_009/escenario

### Situación inicial

Bienvenido al centro IZAR. Lee las instrucciones y usa COMPROBAR al terminar cada paso.

### Etapa 1 de 4

**Enunciado**

Consulta SHUTDOWN /?. En este juego las órdenes de apagado se contestan como texto: no las ejecutes. ¿Qué orden apagaría en 60 segundos con el mensaje El equipo se apagara en un minuto?

**Desarrollo resuelto**

```bat
SHUTDOWN /?
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Orden completa, solo como respuesta:»: `shutdown /s /t 60 /c "El equipo se apagara en un minuto"`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 2 de 4

**Enunciado**

¿Cómo se cancela un apagado pendiente? Responde sin programar uno.

**Desarrollo resuelto**

```bat
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Orden de cancelación:»: `shutdown /a`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 3 de 4

**Enunciado**

Práctica gráfica: escritorio > Nuevo > Acceso directo. Destino: cmd.exe. Nombre: Simbolo del sistema. Ábrelo y ciérralo con EXIT. El profesor revisa el acceso; el motor solo pregunta su destino. No uses un .bat para sustituir el acceso directo.

**Desarrollo resuelto**

```bat
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Destino del acceso directo:»: `cmd.exe`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 4 de 4

**Enunciado**

Diseña los destinos de dos accesos llamados Apagar y No apagar. Apagar: 20 segundos y mensaje Apagando...; No apagar: cancelar. No los abras durante el juego. Creación, iconos y anclaje se revisan con la ficha docente, porque dependen del escritorio y las políticas de Windows.

**Desarrollo resuelto**

```bat
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Destino de Apagar:»: `shutdown /s /t 20 /c "Apagando..."`.
- Respuesta a «Destino de No apagar:»: `shutdown /a`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.


## Juego 10 Tu primer archivo bat

Escenario: datos/actividad_010/escenario

### Situación inicial

Bienvenido al centro IZAR. Lee las instrucciones y usa COMPROBAR al terminar cada paso.

### Etapa 1 de 4

**Enunciado**

Un .bat contiene órdenes de CMD. Lee plantilla.txt. @echo off oculta las órdenes; ECHO escribe mensajes. Copia la plantilla como informe.bat.

**Desarrollo resuelto**

```bat
TYPE plantilla.txt
COPY plantilla.txt informe.bat
COMPROBAR
```

**Qué comprueba**

- `informe.bat` debe conservar el contenido inicial de `plantilla.txt`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 2 de 4

**Enunciado**

Ejecuta CALL informe.bat. CALL permite regresar al script que lo invoca; en CMD interactivo también puedes escribir informe.bat. Revisa version.txt.

**Desarrollo resuelto**

```bat
CALL informe.bat
TYPE version.txt
COMPROBAR
```

**Qué comprueba**

- `version.txt` debe contener la salida de la consulta version.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 3 de 4

**Enunciado**

Crea inicio.bat con un editor de texto (NOTEPAD inicio.bat). Debe contener exactamente estas tres líneas: @echo off, call informe.bat, echo LISTO > listo.txt. Guarda como .bat, no .bat.txt. La comprobación inspecciona el archivo, no lo ejecuta.

**Desarrollo resuelto**

```bat
NOTEPAD inicio.bat
# Contenido / Edukia:
@echo off
call informe.bat
echo LISTO > listo.txt
# Guarda y vuelve a CMD / Gorde eta itzuli CMDra
COMPROBAR
```

**Qué comprueba**

- `inicio.bat` debe contener estas líneas, en orden: `@echo off`; `call informe.bat`; `echo LISTO > listo.txt`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 4 de 4

**Enunciado**

Ejecuta CALL inicio.bat. Debe volver del primer script y escribir LISTO en listo.txt.

**Desarrollo resuelto**

```bat
CALL inicio.bat
TYPE listo.txt
COMPROBAR
```

**Qué comprueba**

- `listo.txt` debe contener estas líneas, en orden: `LISTO`.
- `version.txt` debe contener la salida de la consulta version.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.


## Juego 11 El relevo del técnico

Escenario: datos/actividad_011/escenario

### Situación inicial

Bienvenido al centro IZAR. Lee las instrucciones y usa COMPROBAR al terminar cada paso.

### Etapa 1 de 4

**Enunciado**

Encuentra y lee la nota dentro de Documentos del turno. Usa comillas o Tab para los espacios del nombre.

**Desarrollo resuelto**

```bat
TYPE "Documentos del turno\nota.txt"
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Clave:»: `RELEVO`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 2 de 4

**Enunciado**

Crea entrega. Copia la nota allí como instrucciones.txt conservando el original.

**Desarrollo resuelto**

```bat
MD entrega
COPY "Documentos del turno\nota.txt" entrega\instrucciones.txt
COMPROBAR
```

**Qué comprueba**

- `entrega/instrucciones.txt` debe conservar el contenido inicial de `Documentos del turno/nota.txt`.
- `Documentos del turno/nota.txt` debe conservar el contenido inicial de `Documentos del turno/nota.txt`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 3 de 4

**Enunciado**

Añade a entrega el informe de versión (version.txt) y el de volumen (volumen.txt).

**Desarrollo resuelto**

```bat
VER > entrega\version.txt
VOL %SystemDrive% > entrega\volumen.txt
COMPROBAR
```

**Qué comprueba**

- `entrega/version.txt` debe contener la salida de la consulta version.
- `entrega/volumen.txt` debe contener la salida de la consulta volumen.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 4 de 4

**Enunciado**

Personaliza el prompt a [TURNO] seguido de ruta y >. Después comprueba la entrega.

**Desarrollo resuelto**

```bat
PROMPT [TURNO] $P$G
COMPROBAR
```

**Qué comprueba**

- El entorno CMD debe tener PROMPT igual a `[TURNO] $P$G`.
- `entrega/instrucciones.txt` debe conservar el contenido inicial de `Documentos del turno/nota.txt`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.


## Juego 12 Operación IZAR — Misión final

Escenario: datos/actividad_012/escenario

### Situación inicial

Operación IZAR. Recupera el expediente y aísla el paquete NIEBLA-42. La primera clave está en archivo\orden.txt.

### Etapa 1 de 12

**Enunciado**

Investiga el escenario y encuentra la primera clave. No recibes el comando directamente: combina lo aprendido.

**Desarrollo resuelto**

```bat
TYPE LEEME.txt
TYPE archivo\orden.txt
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Clave:»: `IZAR-2028`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 2 de 12

**Enunciado**

Crea expediente y cuarentena. Copia fuentes\aviso.txt a expediente conservando el original.

**Desarrollo resuelto**

```bat
MD expediente
MD cuarentena
COPY fuentes\aviso.txt expediente\
COMPROBAR
```

**Qué comprueba**

- Debe existir la carpeta `cuarentena`.
- `expediente/aviso.txt` debe conservar el contenido inicial de `fuentes/aviso.txt`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 3 de 12

**Enunciado**

Consulta la ayuda de SYSTEMINFO y ejecuta la consulta. Identifica el nombre de este equipo.

**Desarrollo resuelto**

```bat
SYSTEMINFO /?
SYSTEMINFO
COMPROBAR
```

**Qué comprueba**

- Compara la respuesta con la consulta real: equipo. Copia la salida de la VM, no un ejemplo.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 4 de 12

**Enunciado**

Deja la versión de Windows en expediente\version.txt, sin añadir títulos ni etiquetas.

**Desarrollo resuelto**

```bat
VER > expediente\version.txt
COMPROBAR
```

**Qué comprueba**

- `expediente/version.txt` debe contener la salida de la consulta version.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 5 de 12

**Enunciado**

Consulta fecha y hora sin cambiarlas. Responde con ambas órdenes, una por pregunta.

**Desarrollo resuelto**

```bat
DATE /T
TIME /T
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Orden para la fecha:»: `DATE /T`.
- Respuesta a «Orden para la hora:»: `TIME /T`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 6 de 12

**Enunciado**

Guarda la información del volumen del sistema en expediente\volumen.txt. No cambies su etiqueta.

**Desarrollo resuelto**

```bat
VOL %SystemDrive% > expediente\volumen.txt
COMPROBAR
```

**Qué comprueba**

- `expediente/volumen.txt` debe contener la salida de la consulta volumen.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 7 de 12

**Enunciado**

Personaliza el prompt con [IZAR] seguido de la ruta y >. Cambia el título a Operacion IZAR y consulta PATH sin alterarlo. Solo se valida automáticamente el prompt y la respuesta conceptual.

**Desarrollo resuelto**

```bat
PROMPT [IZAR] $P$G
TITLE Operacion IZAR
PATH
COMPROBAR
```

**Qué comprueba**

- El entorno CMD debe tener PROMPT igual a `[IZAR] $P$G`.
- Respuesta a «Comando que cambia el título:»: `TITLE`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 8 de 12

**Enunciado**

Investiga los paquetes. Mueve el que tiene NIEBLA-42 a cuarentena\sospechoso.txt. Conserva normal.txt.

**Desarrollo resuelto**

```bat
TYPE archivo\paquetes\resumen.txt
TYPE archivo\paquetes\normal.txt
MOVE archivo\paquetes\resumen.txt cuarentena\sospechoso.txt
COMPROBAR
```

**Qué comprueba**

- `cuarentena/sospechoso.txt` debe conservar el contenido inicial de `archivo/paquetes/resumen.txt`.
- No debe existir `archivo/paquetes/resumen.txt`.
- `archivo/paquetes/normal.txt` debe conservar el contenido inicial de `archivo/paquetes/normal.txt`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 9 de 12

**Enunciado**

Planifica, sin ejecutar: apagado en 60 segundos; cancelación; comprobación de C: sin solicitar reparaciones.

**Desarrollo resuelto**

```bat
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Apagado:»: `shutdown /s /t 60`.
- Respuesta a «Cancelación:»: `shutdown /a`.
- Respuesta a «Comprobación de disco:»: `chkdsk C:`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 10 de 12

**Enunciado**

Crea cierre.bat con cuatro líneas exactas: desactiva eco, genera versión, genera volumen y escribe LISTO en expediente\listo.txt. Consulta PISTA para ver la plantilla completa. No incluyas apagado ni reparación.

**Desarrollo resuelto**

```bat
NOTEPAD cierre.bat
# Contenido / Edukia:
@echo off
ver > expediente\version.txt
vol %SystemDrive% > expediente\volumen.txt
echo LISTO > expediente\listo.txt
# Guarda y vuelve a CMD / Gorde eta itzuli CMDra
COMPROBAR
```

**Qué comprueba**

- `cierre.bat` debe contener estas líneas, en orden: `@echo off`; `ver > expediente\version.txt`; `vol %SystemDrive% > expediente\volumen.txt`; `echo LISTO > expediente\listo.txt`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 11 de 12

**Enunciado**

Ejecuta cierre.bat desde la raíz del escenario. COMPROBAR revisará todo el expediente, no solo el último archivo.

**Desarrollo resuelto**

```bat
CALL cierre.bat
COMPROBAR
```

**Qué comprueba**

- `expediente/aviso.txt` debe conservar el contenido inicial de `fuentes/aviso.txt`.
- `fuentes/aviso.txt` debe conservar el contenido inicial de `fuentes/aviso.txt`.
- `cuarentena/sospechoso.txt` debe conservar el contenido inicial de `archivo/paquetes/resumen.txt`.
- No debe existir `archivo/paquetes/resumen.txt`.
- `archivo/paquetes/normal.txt` debe conservar el contenido inicial de `archivo/paquetes/normal.txt`.
- `expediente/version.txt` debe contener la salida de la consulta version.
- `expediente/volumen.txt` debe contener la salida de la consulta volumen.
- `expediente/listo.txt` debe contener estas líneas, en orden: `LISTO`.
- `cierre.bat` debe contener estas líneas, en orden: `@echo off`; `ver > expediente\version.txt`; `vol %SystemDrive% > expediente\volumen.txt`; `echo LISTO > expediente\listo.txt`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.

### Etapa 12 de 12

**Enunciado**

Sal con EXIT y vuelve a esta actividad. Comprueba que el expediente sigue completo. No uses REINICIAR.

**Desarrollo resuelto**

```bat
EXIT
# Volver a la actividad 12 / Itzuli 12. jarduerara
COMPROBAR
```

**Qué comprueba**

- Debe abrirse otra sesión después del paso anterior. MENU también sirve para la comprobación; EXIT es la práctica solicitada.
- `expediente/aviso.txt` debe conservar el contenido inicial de `fuentes/aviso.txt`.
- `fuentes/aviso.txt` debe conservar el contenido inicial de `fuentes/aviso.txt`.
- `cuarentena/sospechoso.txt` debe conservar el contenido inicial de `archivo/paquetes/resumen.txt`.
- No debe existir `archivo/paquetes/resumen.txt`.
- `archivo/paquetes/normal.txt` debe conservar el contenido inicial de `archivo/paquetes/normal.txt`.
- `expediente/version.txt` debe contener la salida de la consulta version.
- `expediente/volumen.txt` debe contener la salida de la consulta volumen.
- `expediente/listo.txt` debe contener estas líneas, en orden: `LISTO`.
- `cierre.bat` debe contener estas líneas, en orden: `@echo off`; `ver > expediente\version.txt`; `vol %SystemDrive% > expediente\volumen.txt`; `echo LISTO > expediente\listo.txt`.

**Primera pista:** Lee la ayuda del comando y revisa la carpeta actual.


## Juego 13 Extra — Adivina el comando

Escenario: datos/actividad_013/escenario

### Situación inicial

Bienvenido al centro IZAR. Lee las instrucciones y usa COMPROBAR al terminar cada paso.

### Etapa 1 de 30

**Enunciado**

Definición 1: Muestra la carpeta actual. Escribe COMPROBAR y responde como texto; no ejecutes la respuesta.

**Desarrollo resuelto**

```bat
CD
```

**Qué comprueba**

- Respuesta a «Respuesta:»: `CD`.

**Primera pista:** Inicial: C

### Etapa 2 de 30

**Enunciado**

Definición 2: Lista archivos y carpetas. Escribe COMPROBAR y responde como texto; no ejecutes la respuesta.

**Desarrollo resuelto**

```bat
DIR
```

**Qué comprueba**

- Respuesta a «Respuesta:»: `DIR`.

**Primera pista:** Inicial: D

### Etapa 3 de 30

**Enunciado**

Definición 3: Muestra el contenido de un archivo de texto. Escribe COMPROBAR y responde como texto; no ejecutes la respuesta.

**Desarrollo resuelto**

```bat
TYPE
```

**Qué comprueba**

- Respuesta a «Respuesta:»: `TYPE`.

**Primera pista:** Inicial: T

### Etapa 4 de 30

**Enunciado**

Definición 4: Crea una carpeta. Escribe COMPROBAR y responde como texto; no ejecutes la respuesta.

**Desarrollo resuelto**

```bat
MD
```

**Qué comprueba**

- Respuesta a «Respuesta:»: `MD` / `MKDIR`.

**Primera pista:** Inicial: M

### Etapa 5 de 30

**Enunciado**

Definición 5: Copia conservando el original. Escribe COMPROBAR y responde como texto; no ejecutes la respuesta.

**Desarrollo resuelto**

```bat
COPY
```

**Qué comprueba**

- Respuesta a «Respuesta:»: `COPY`.

**Primera pista:** Inicial: C

### Etapa 6 de 30

**Enunciado**

Definición 6: Mueve archivos. Escribe COMPROBAR y responde como texto; no ejecutes la respuesta.

**Desarrollo resuelto**

```bat
MOVE
```

**Qué comprueba**

- Respuesta a «Respuesta:»: `MOVE`.

**Primera pista:** Inicial: M

### Etapa 7 de 30

**Enunciado**

Definición 7: Cambia el nombre de un archivo. Escribe COMPROBAR y responde como texto; no ejecutes la respuesta.

**Desarrollo resuelto**

```bat
REN
```

**Qué comprueba**

- Respuesta a «Respuesta:»: `REN` / `RENAME`.

**Primera pista:** Inicial: R

### Etapa 8 de 30

**Enunciado**

Definición 8: Muestra la ayuda general. Escribe COMPROBAR y responde como texto; no ejecutes la respuesta.

**Desarrollo resuelto**

```bat
HELP
```

**Qué comprueba**

- Respuesta a «Respuesta:»: `HELP`.

**Primera pista:** Inicial: H

### Etapa 9 de 30

**Enunciado**

Definición 9: Opción habitual para pedir ayuda. Escribe COMPROBAR y responde como texto; no ejecutes la respuesta.

**Desarrollo resuelto**

```bat
/?
```

**Qué comprueba**

- Respuesta a «Respuesta:»: `/?`.

**Primera pista:** Inicial: /

### Etapa 10 de 30

**Enunciado**

Definición 10: Limpia la pantalla. Escribe COMPROBAR y responde como texto; no ejecutes la respuesta.

**Desarrollo resuelto**

```bat
CLS
```

**Qué comprueba**

- Respuesta a «Respuesta:»: `CLS`.

**Primera pista:** Inicial: C

### Etapa 11 de 30

**Enunciado**

Definición 11: Muestra la versión de Windows. Escribe COMPROBAR y responde como texto; no ejecutes la respuesta.

**Desarrollo resuelto**

```bat
VER
```

**Qué comprueba**

- Respuesta a «Respuesta:»: `VER`.

**Primera pista:** Inicial: V

### Etapa 12 de 30

**Enunciado**

Definición 12: Consulta fecha sin pedir una nueva. Escribe COMPROBAR y responde como texto; no ejecutes la respuesta.

**Desarrollo resuelto**

```bat
DATE /T
```

**Qué comprueba**

- Respuesta a «Respuesta:»: `DATE /T`.

**Primera pista:** Inicial: D

### Etapa 13 de 30

**Enunciado**

Definición 13: Consulta hora sin pedir una nueva. Escribe COMPROBAR y responde como texto; no ejecutes la respuesta.

**Desarrollo resuelto**

```bat
TIME /T
```

**Qué comprueba**

- Respuesta a «Respuesta:»: `TIME /T`.

**Primera pista:** Inicial: T

### Etapa 14 de 30

**Enunciado**

Definición 14: Cambia el título de CMD. Escribe COMPROBAR y responde como texto; no ejecutes la respuesta.

**Desarrollo resuelto**

```bat
TITLE
```

**Qué comprueba**

- Respuesta a «Respuesta:»: `TITLE`.

**Primera pista:** Inicial: T

### Etapa 15 de 30

**Enunciado**

Definición 15: Cambia los colores de CMD. Escribe COMPROBAR y responde como texto; no ejecutes la respuesta.

**Desarrollo resuelto**

```bat
COLOR
```

**Qué comprueba**

- Respuesta a «Respuesta:»: `COLOR`.

**Primera pista:** Inicial: C

### Etapa 16 de 30

**Enunciado**

Definición 16: Personaliza el indicador de órdenes. Escribe COMPROBAR y responde como texto; no ejecutes la respuesta.

**Desarrollo resuelto**

```bat
PROMPT
```

**Qué comprueba**

- Respuesta a «Respuesta:»: `PROMPT`.

**Primera pista:** Inicial: P

### Etapa 17 de 30

**Enunciado**

Definición 17: Muestra las rutas de búsqueda de ejecutables. Escribe COMPROBAR y responde como texto; no ejecutes la respuesta.

**Desarrollo resuelto**

```bat
PATH
```

**Qué comprueba**

- Respuesta a «Respuesta:»: `PATH`.

**Primera pista:** Inicial: P

### Etapa 18 de 30

**Enunciado**

Definición 18: Abre otra ventana para un programa. Escribe COMPROBAR y responde como texto; no ejecutes la respuesta.

**Desarrollo resuelto**

```bat
START
```

**Qué comprueba**

- Respuesta a «Respuesta:»: `START`.

**Primera pista:** Inicial: S

### Etapa 19 de 30

**Enunciado**

Definición 19: Inicia el intérprete de comandos. Escribe COMPROBAR y responde como texto; no ejecutes la respuesta.

**Desarrollo resuelto**

```bat
CMD
```

**Qué comprueba**

- Respuesta a «Respuesta:»: `CMD` / `CMD.EXE`.

**Primera pista:** Inicial: C

### Etapa 20 de 30

**Enunciado**

Definición 20: Sale del intérprete actual. Escribe COMPROBAR y responde como texto; no ejecutes la respuesta.

**Desarrollo resuelto**

```bat
EXIT
```

**Qué comprueba**

- Respuesta a «Respuesta:»: `EXIT`.

**Primera pista:** Inicial: E

### Etapa 21 de 30

**Enunciado**

Definición 21: Muestra información detallada del sistema. Escribe COMPROBAR y responde como texto; no ejecutes la respuesta.

**Desarrollo resuelto**

```bat
SYSTEMINFO
```

**Qué comprueba**

- Respuesta a «Respuesta:»: `SYSTEMINFO`.

**Primera pista:** Inicial: S

### Etapa 22 de 30

**Enunciado**

Definición 22: Muestra etiqueta y número de serie del volumen. Escribe COMPROBAR y responde como texto; no ejecutes la respuesta.

**Desarrollo resuelto**

```bat
VOL
```

**Qué comprueba**

- Respuesta a «Respuesta:»: `VOL`.

**Primera pista:** Inicial: V

### Etapa 23 de 30

**Enunciado**

Definición 23: Permite cambiar la etiqueta de un volumen. Escribe COMPROBAR y responde como texto; no ejecutes la respuesta.

**Desarrollo resuelto**

```bat
LABEL
```

**Qué comprueba**

- Respuesta a «Respuesta:»: `LABEL`.

**Primera pista:** Inicial: L

### Etapa 24 de 30

**Enunciado**

Definición 24: Comprueba el sistema de archivos del disco. Escribe COMPROBAR y responde como texto; no ejecutes la respuesta.

**Desarrollo resuelto**

```bat
CHKDSK
```

**Qué comprueba**

- Respuesta a «Respuesta:»: `CHKDSK`.

**Primera pista:** Inicial: C

### Etapa 25 de 30

**Enunciado**

Definición 25: Gestiona el apagado del sistema. Solo responde el nombre. Escribe COMPROBAR y responde como texto; no ejecutes la respuesta.

**Desarrollo resuelto**

```bat
SHUTDOWN
```

**Qué comprueba**

- Respuesta a «Respuesta:»: `SHUTDOWN`.

**Primera pista:** Inicial: S

### Etapa 26 de 30

**Enunciado**

Definición 26: Cancela un apagado pendiente. Escribe COMPROBAR y responde como texto; no ejecutes la respuesta.

**Desarrollo resuelto**

```bat
SHUTDOWN /A
```

**Qué comprueba**

- Respuesta a «Respuesta:»: `SHUTDOWN /A`.

**Primera pista:** Inicial: S

### Etapa 27 de 30

**Enunciado**

Definición 27: Llama a otro .bat y permite regresar al primero. Escribe COMPROBAR y responde como texto; no ejecutes la respuesta.

**Desarrollo resuelto**

```bat
CALL
```

**Qué comprueba**

- Respuesta a «Respuesta:»: `CALL`.

**Primera pista:** Inicial: C

### Etapa 28 de 30

**Enunciado**

Definición 28: Muestra un mensaje en pantalla. Escribe COMPROBAR y responde como texto; no ejecutes la respuesta.

**Desarrollo resuelto**

```bat
ECHO
```

**Qué comprueba**

- Respuesta a «Respuesta:»: `ECHO`.

**Primera pista:** Inicial: E

### Etapa 29 de 30

**Enunciado**

Definición 29: Extensión de los scripts de esta unidad, incluido el punto. Escribe COMPROBAR y responde como texto; no ejecutes la respuesta.

**Desarrollo resuelto**

```bat
.BAT
```

**Qué comprueba**

- Respuesta a «Respuesta:»: `.BAT`.

**Primera pista:** Inicial: .

### Etapa 30 de 30

**Enunciado**

Definición 30: Símbolo que guarda salida sobrescribiendo un archivo. Escribe COMPROBAR y responde como texto; no ejecutes la respuesta.

**Desarrollo resuelto**

```bat
>
```

**Qué comprueba**

- Respuesta a «Respuesta:»: `>`.

**Primera pista:** Inicial: >

## Dudas frecuentes

- No reconoce COMPROBAR: entra desde jugar.bat y no sobrescribas PATH. Volver al menú y entrar restaura las rutas.
- Un .bat no vuelve al primero: usa CALL.
- Se guarda como .bat.txt: muestra extensiones y guarda como todos los archivos en el editor.
- Prompt incorrecto: usa $P y $G; vuelve a establecerlo si has salido de la actividad.
- Ruta con espacios: utiliza comillas; cambiar de unidad requiere CD /D.
- Archivo vacío: TYPE NUL > archivo crea cero bytes. ECHO. crea una línea.
- Fecha incorrecta: consulta DATE /T justo antes de comprobar.
- Acentos: inicia con jugar.bat, que selecciona UTF-8. Los informes admiten también UTF-16 y OEM.
- START confunde ruta y título: su primer argumento entre comillas es el título.
- No permite anclar acceso: depende de Windows y políticas; documenta la limitación.
- CHKDSK pide permisos: se ejecuta aparte con el profesor, no elevando el juego.
- No actualiza: publica el repo y configura url_base. ACTUALIZAR no sustituye el motor.
- Actividad antigua tras actualizar: conserva su definición hasta REINICIAR.
- Cambiar idioma no traduce archivos existentes: reinicia solo la actividad de prueba para regenerarlos.

## Prácticas externas

Consulta PRACTICAS_SUPERVISADAS.md para accesos directos, apagado, USB y CHKDSK. Las respuestas no certifican esas acciones. Los JSON contienen soluciones accesibles: práctica, no examen protegido.

## Fuentes

- 3.2- Intro de Windows en comandos.pdf, aportado por el docente.
- 3.2.1- Actividades de Windows en comandos.odt, aportado por el docente.
- Microsoft Learn: https://learn.microsoft.com/windows-server/administration/windows-commands/windows-commands
