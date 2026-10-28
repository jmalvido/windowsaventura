# Guía docente de WindowsAventura 0.2

# Paleo Isla

12 misiones independientes y un extra de 17 definiciones. Enunciados y soluciones en castellano; el juego incluye también euskera.

## Alcance de la unidad

Comandos del material: CHKDSK, CLS, CMD, COLOR, DATE, EXIT, HELP, LABEL, PATH, PROMPT, SHUTDOWN, SYSTEMINFO, START, TIME, TITLE, VER y VOL.
No hay ejercicios de creación de scripts, archivos o carpetas ni redirecciones. Los lanzadores .bat son infraestructura del juego. La narración se muestra en pantalla.

## Cómo consultar la guía

Busca juego y etapa. Las soluciones muestran las consultas o acciones propuestas; las respuestas aparecen en Qué comprueba. Las líneas REM son notas de la guía, no tareas nuevas. No ejecutes las respuestas de apagado, etiqueta o reparación: introdúcelas solo cuando COMPROBAR pregunte.
El corrector compara respuestas con datos reales de la VM cuando corresponde. Título, color, teclas y acciones gráficas necesitan observación del profesor; una respuesta correcta no certifica su ejecución.

## Mapa de misiones

| Nº | Misión | Etapas |
|---|---|---|
| 1 | Bienvenido a Paleo Isla — La consola del visitante | 3 |
| 2 | Bienvenido a Paleo Isla — El reloj de la expedición | 3 |
| 3 | Bienvenido a Paleo Isla — Tu puesto de guardia | 3 |
| 4 | La ficha del laboratorio de fósiles | 3 |
| 5 | El turno de las incubadoras | 3 |
| 6 | El archivo de huellas | 3 |
| 7 | El disco de las cámaras de los estegosaurios | 3 |
| 8 | Las rutas de la estación de rastreo | 3 |
| 9 | Una segunda torre de observación | 3 |
| 10 | El cierre del centro de visitantes | 3 |
| 11 | Los accesos del puesto de los velociraptores | 3 |
| 12 | La gran reapertura de Paleo Isla | 12 |
| 13 | Extra — El examen de los guardas del parque | 17 |

## Juego 1 Bienvenido a Paleo Isla — La consola del visitante

Llegas a Paleo Isla como técnico en prácticas. Antes de entrar en los recintos, aprende a pedir ayuda al terminal. Todo se lee en pantalla; no necesitas abrir archivos.

Comandos: HELP, COLOR, CLS.

### Etapa 1 de 3

**Enunciado**

El puesto de recepción necesita su catálogo de órdenes. Ejecuta HELP. En las respuestas introduce el comando, no toda la salida. Después escribe COMPROBAR.

**Desarrollo**

```bat
HELP
COMPROBAR
```

**Qué comprueba**

- Respuesta a «¿Qué comando muestra la ayuda general?»: `HELP`.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.

### Etapa 2 de 3

**Enunciado**

La cuidadora quiere consultar los colores disponibles. Ejecuta COLOR /?. La ayuda también puede pedirse con HELP COLOR. Después escribe COMPROBAR.

**Desarrollo**

```bat
COLOR /?
HELP COLOR
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Opción de ayuda que acompaña a COLOR:»: `/?`.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.

### Etapa 3 de 3

**Enunciado**

La pantalla de recepción está llena de consultas. Ejecuta CLS para despejarla y vuelve a escribir COMPROBAR; el objetivo reaparece con AYUDA si lo necesitas. Después escribe COMPROBAR.

**Desarrollo**

```bat
CLS
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Comando para limpiar la pantalla:»: `CLS`.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.


## Juego 2 Bienvenido a Paleo Isla — El reloj de la expedición

La expedición a la zona de los diplodocus sale hoy. Revisa el equipo y su reloj sin cambiar ninguna configuración.

Comandos: VER, DATE, TIME.

### Etapa 1 de 3

**Enunciado**

VER muestra la versión de Windows del puesto. Ejecuta VER y copia su línea completa cuando se te pregunte. Después escribe COMPROBAR.

**Desarrollo**

```bat
VER
COMPROBAR
```

**Qué comprueba**

- Respuesta comparada con la consulta real version. Debe corresponder a la máquina del alumno.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.

### Etapa 2 de 3

**Enunciado**

Ejecuta DATE /T. /T permite consultar sin pedir una fecha nueva. Copia la salida completa, incluido el día de la semana si aparece. Después escribe COMPROBAR.

**Desarrollo**

```bat
DATE /T
COMPROBAR
```

**Qué comprueba**

- Respuesta comparada con la consulta real fecha. Debe corresponder a la máquina del alumno.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.

### Etapa 3 de 3

**Enunciado**

Ejecuta TIME /T y observa la hora. Usa flecha arriba para recuperar la orden y repetirla. No se evalúa la pulsación de la tecla. Después escribe COMPROBAR.

**Desarrollo**

```bat
TIME /T
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Orden para consultar la hora sin modificarla:»: `TIME /T`.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.


## Juego 3 Bienvenido a Paleo Isla — Tu puesto de guardia

Te asignan la torre de vigilancia de los triceratops. Personaliza la consola para reconocer el puesto.

Comandos: TITLE, COLOR, PROMPT.

### Etapa 1 de 3

**Enunciado**

TITLE cambia el título de la ventana. Ejecuta TITLE Torre Triceratops y observa el resultado. La revisión del título es visual. Después escribe COMPROBAR.

**Desarrollo**

```bat
TITLE Torre Triceratops
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Orden utilizada:»: `TITLE Torre Triceratops`.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.

### Etapa 2 de 3

**Enunciado**

Consulta COLOR /?. Pon fondo azul y letras rojas con COLOR 14. El primer dígito indica el fondo y el segundo el texto. Después restaura COLOR 0B. Después escribe COMPROBAR.

**Desarrollo**

```bat
COLOR /?
COLOR 14
COLOR 0B
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Código para fondo azul y letras rojas:»: `14`.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.

### Etapa 3 de 3

**Enunciado**

PROMPT cambia el indicador donde escribes. Ejecuta PROMPT [TRICERATOPS] $P$G. $P representa la ruta y $G el signo de cierre. Después escribe COMPROBAR.

**Desarrollo**

```bat
PROMPT [TRICERATOPS] $P$G
COMPROBAR
```

**Qué comprueba**

- PROMPT debe ser `[TRICERATOPS] $P$G` en el entorno real.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.


## Juego 4 La ficha del laboratorio de fósiles

El laboratorio de fósiles ha recibido una estación de trabajo sin inventariar. Debes identificarla antes de catalogar las muestras.

Comandos: SYSTEMINFO, VER, HELP.

### Etapa 1 de 3

**Enunciado**

Busca la ayuda del comando que muestra información detallada del sistema. Después escribe COMPROBAR.

**Desarrollo**

```bat
SYSTEMINFO /?
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Orden de ayuda:»: `SYSTEMINFO /?` / `HELP SYSTEMINFO`.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.

### Etapa 2 de 3

**Enunciado**

Ejecuta esa consulta y localiza el nombre del equipo. Puede tardar. Responde solo con el nombre, sin la etiqueta que lo precede. Después escribe COMPROBAR.

**Desarrollo**

```bat
SYSTEMINFO
COMPROBAR
```

**Qué comprueba**

- Respuesta comparada con la consulta real equipo. Debe corresponder a la máquina del alumno.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.

### Etapa 3 de 3

**Enunciado**

Localiza sistema operativo y memoria en la salida anterior. El profesor revisará tu interpretación. Consulta también la versión con la orden breve y copia su resultado. Después escribe COMPROBAR.

**Desarrollo**

```bat
VER
COMPROBAR
```

**Qué comprueba**

- Respuesta comparada con la consulta real version. Debe corresponder a la máquina del alumno.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.


## Juego 5 El turno de las incubadoras

Los cuidadores anotan la revisión de los huevos de dinosaurio. Hay que consultar fecha y hora sin alterar el reloj del puesto.

Comandos: DATE, TIME, CLS.

### Etapa 1 de 3

**Enunciado**

Comprueba en la ayuda qué opción evita solicitar una fecha nueva. Después escribe COMPROBAR.

**Desarrollo**

```bat
DATE /?
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Opción de consulta:»: `/T`.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.

### Etapa 2 de 3

**Enunciado**

La ficha de las incubadoras necesita la fecha real de esta máquina. Obtén la salida completa. Después escribe COMPROBAR.

**Desarrollo**

```bat
DATE /T
COMPROBAR
```

**Qué comprueba**

- Respuesta comparada con la consulta real fecha. Debe corresponder a la máquina del alumno.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.

### Etapa 3 de 3

**Enunciado**

Comprueba la hora sin iniciar un cambio y recupera la consulta con flecha arriba. Después limpia la pantalla para el siguiente cuidador. Después escribe COMPROBAR.

**Desarrollo**

```bat
TIME /T
CLS
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Orden de consulta de hora:»: `TIME /T`.
- Respuesta a «Orden de limpieza:»: `CLS`.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.


## Juego 6 El archivo de huellas

El equipo de campo vuelve con fotografías de huellas. Antes de usar un soporte, hay que distinguir su etiqueta y número de serie.

Comandos: VOL, LABEL.

### Etapa 1 de 3

**Enunciado**

Consulta el volumen del sistema con VOL. Observa etiqueta y número de serie; no cambies ninguno. Después escribe COMPROBAR.

**Desarrollo**

```bat
VOL
COMPROBAR
```

**Qué comprueba**

- Respuesta a «¿Qué comando muestra etiqueta y número de serie?»: `VOL`.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.

### Etapa 2 de 3

**Enunciado**

Consulta LABEL /?. El USB de ejemplo se llama E:, pero no asumas que esa letra corresponde a un USB real. Diseña como texto la orden que le asignaría HUELLAS. Después escribe COMPROBAR.

**Desarrollo**

```bat
LABEL /?
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Orden de ejemplo, sin ejecutarla:»: `LABEL E: HUELLAS`.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.

### Etapa 3 de 3

**Enunciado**

El profesor puede proponer la práctica con un USB identificado. Para el juego, indica cómo consultarías E: después del cambio sin modificarla otra vez. Después escribe COMPROBAR.

**Desarrollo**

```bat
VOL /?
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Consulta del volumen E:»: `VOL E:`.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.


## Juego 7 El disco de las cámaras de los estegosaurios

La estación de cámaras necesita un diagnóstico de almacenamiento. Tu misión es escoger la consulta adecuada, no reparar el disco.

Comandos: CHKDSK, HELP.

### Etapa 1 de 3

**Enunciado**

Consulta la ayuda de CHKDSK. La ejecución real se realiza aparte con el profesor en un CMD elevado; no eleves el juego. Después escribe COMPROBAR.

**Desarrollo**

```bat
CHKDSK /?
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Comando que comprueba el sistema de archivos:»: `CHKDSK`.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.

### Etapa 2 de 3

**Enunciado**

Diseña la orden para consultar C: sin solicitar reparación. Responde como texto, sin ejecutarla en el juego. Después escribe COMPROBAR.

**Desarrollo**

```bat
CHKDSK /?
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Orden de consulta:»: `CHKDSK C:`.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.

### Etapa 3 de 3

**Enunciado**

Distingue diagnóstico y reparación. Identifica en la ayuda la opción que solicita corregir errores; no la ejecutes. Después escribe COMPROBAR.

**Desarrollo**

```bat
HELP CHKDSK
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Opción que solicita reparar:»: `/F`.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.


## Juego 8 Las rutas de la estación de rastreo

Los rastreadores quieren entender cómo localiza programas su consola. Debes consultar sus rutas sin alterar la configuración.

Comandos: PATH, CMD, VER.

### Etapa 1 de 3

**Enunciado**

Consulta PATH sin argumentos. Observa que contiene varios directorios. No sustituyas su contenido. Después escribe COMPROBAR.

**Desarrollo**

```bat
PATH
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Separador entre directorios:»: `;`.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.

### Etapa 2 de 3

**Enunciado**

Consulta CMD /?. Averigua qué opción ejecuta una orden y cierra ese intérprete. Después escribe COMPROBAR.

**Desarrollo**

```bat
CMD /?
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Opción que ejecuta y termina:»: `/C`.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.

### Etapa 3 de 3

**Enunciado**

Usa un intérprete temporal para consultar la versión: CMD /C VER. Al terminar vuelves a tu consola. Después escribe COMPROBAR.

**Desarrollo**

```bat
CMD /C VER
COMPROBAR
```

**Qué comprueba**

- Respuesta comparada con la consulta real version. Debe corresponder a la máquina del alumno.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.


## Juego 9 Una segunda torre de observación

Necesitas una segunda consola para observar el sector de los diplodocus sin cerrar el puesto principal.

Comandos: START, CMD, VER, EXIT.

### Etapa 1 de 3

**Enunciado**

Consulta START /?. Recuerda que su primer texto entre comillas se utiliza como título. Después escribe COMPROBAR.

**Desarrollo**

```bat
START /?
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Comando que abre otra ventana para un programa:»: `START`.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.

### Etapa 2 de 3

**Enunciado**

Abre otra consola con START "Torre Diplodocus" CMD /K VER. Observa la versión, cierra solo esa consola con EXIT y vuelve aquí. Después escribe COMPROBAR.

**Desarrollo**

```bat
START "Torre Diplodocus" CMD /K VER
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Opción de CMD que mantiene la consola abierta:»: `/K`.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.

### Etapa 3 de 3

**Enunciado**

Entrega el puesto al siguiente observador: sal de ESTA actividad con EXIT, vuelve a seleccionarla y comprueba. No reinicies. Después escribe COMPROBAR.

**Desarrollo**

```bat
EXIT
REM Selecciona otra vez la actividad 9 / Hautatu berriro 9. jarduera
COMPROBAR
```

**Qué comprueba**

- Debe abrirse otra sesión tras superar el paso anterior. Se pide EXIT; MENU también permite superar esta condición.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.


## Juego 10 El cierre del centro de visitantes

El parque cierra, pero los cuidadores siguen trabajando. Prepara el apagado del puesto como una propuesta escrita, sin ejecutarlo.

Comandos: SHUTDOWN.

### Etapa 1 de 3

**Enunciado**

Consulta SHUTDOWN /? y localiza la opción de apagado, diferenciándola de reiniciar. Después escribe COMPROBAR.

**Desarrollo**

```bat
SHUTDOWN /?
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Opción para apagar:»: `/S`.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.

### Etapa 2 de 3

**Enunciado**

Diseña un apagado en 60 segundos con el mensaje El parque cierra en un minuto. Introdúcelo solo como respuesta de COMPROBAR. Después escribe COMPROBAR.

**Desarrollo**

```bat
SHUTDOWN /?
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Orden propuesta, sin ejecutarla:»: `shutdown /s /t 60 /c "El parque cierra en un minuto"`.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.

### Etapa 3 de 3

**Enunciado**

Una cuidadora necesita seguir trabajando. ¿Qué orden cancelaría un apagado pendiente? No programes ninguno para responder. Después escribe COMPROBAR.

**Desarrollo**

```bat
SHUTDOWN /?
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Orden de cancelación:»: `shutdown /a`.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.


## Juego 11 Los accesos del puesto de los velociraptores

El encargado del recinto necesita accesos directos reconocibles en el escritorio. Se crean desde Windows, no mediante scripts.

Comandos: CMD, EXIT, SHUTDOWN.

### Etapa 1 de 3

**Enunciado**

En el escritorio crea un acceso directo con destino cmd.exe y nombre Puesto Velociraptores. Ábrelo y ciérralo con EXIT. El profesor revisa el acceso; el corrector pregunta el destino. Después escribe COMPROBAR.

**Desarrollo**

```bat
REM Escritorio: Nuevo, Acceso directo / Mahaigaina: Berria, Lasterbidea
REM Destino / Helburua: cmd.exe
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Destino del acceso al terminal:»: `cmd.exe`.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.

### Etapa 2 de 3

**Enunciado**

Prepara con el profesor los accesos Apagar y No apagar. Apagar debe esperar 20 segundos y mostrar Apagando...; No apagar debe cancelar. No los abras para comprobar esta etapa. Después escribe COMPROBAR.

**Desarrollo**

```bat
SHUTDOWN /?
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Destino de Apagar:»: `shutdown /s /t 20 /c "Apagando..."`.
- Respuesta a «Destino de No apagar:»: `shutdown /a`.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.

### Etapa 3 de 3

**Enunciado**

Revisa con el profesor el icono y las opciones de anclar los accesos al Inicio o la barra. Dependen de la versión y políticas de Windows. No sustituimos estas acciones por un script. Para cerrar, identifica el comando del intérprete. Después escribe COMPROBAR.

**Desarrollo**

```bat
CMD /?
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Intérprete usado en la unidad:»: `CMD` / `CMD.EXE`.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.


## Juego 12 La gran reapertura de Paleo Isla

Mañana llegan los visitantes. Coordina recepción, incubadoras, cámaras y torres para preparar la reapertura. Las órdenes de mantenimiento se diseñan sin ejecutarlas. Cada etapa pertenece a este mismo turno.

Comandos: HELP, CLS, VER, SYSTEMINFO, DATE, TIME, TITLE, COLOR, PROMPT, PATH, VOL, LABEL, CHKDSK, START, CMD, EXIT, SHUTDOWN.

### Etapa 1 de 12

**Enunciado**

Recepción pide recuperar el catálogo de ayuda y despejar la pantalla antes de iniciar el turno. Elige las dos órdenes. Después escribe COMPROBAR.

**Desarrollo**

```bat
HELP
CLS
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Catálogo de ayuda:»: `HELP`.
- Respuesta a «Limpiar pantalla:»: `CLS`.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.

### Etapa 2 de 12

**Enunciado**

Identifica la versión del puesto de recepción con la consulta breve y copia su salida. Después escribe COMPROBAR.

**Desarrollo**

```bat
VER
COMPROBAR
```

**Qué comprueba**

- Respuesta comparada con la consulta real version. Debe corresponder a la máquina del alumno.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.

### Etapa 3 de 12

**Enunciado**

El laboratorio necesita el nombre del equipo y revisar memoria y sistema operativo. Consulta el informe completo; responde con el nombre. Después escribe COMPROBAR.

**Desarrollo**

```bat
SYSTEMINFO
COMPROBAR
```

**Qué comprueba**

- Respuesta comparada con la consulta real equipo. Debe corresponder a la máquina del alumno.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.

### Etapa 4 de 12

**Enunciado**

Consulta fecha y hora de las incubadoras sin cambiarlas. Copia la fecha y explica con qué orden consultaste la hora. Después escribe COMPROBAR.

**Desarrollo**

```bat
DATE /T
TIME /T
COMPROBAR
```

**Qué comprueba**

- Respuesta comparada con la consulta real fecha. Debe corresponder a la máquina del alumno.
- Respuesta a «Orden de hora:»: `TIME /T`.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.

### Etapa 5 de 12

**Enunciado**

Pon el título Reapertura Paleo Isla. El puesto exige fondo blanco brillante y texto rojo normal: consulta COLOR si lo necesitas. Vuelve a COLOR 0B después de observarlo. Después escribe COMPROBAR.

**Desarrollo**

```bat
TITLE Reapertura Paleo Isla
COLOR F4
COLOR 0B
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Orden de título:»: `TITLE Reapertura Paleo Isla`.
- Respuesta a «Código solicitado:»: `F4`.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.

### Etapa 6 de 12

**Enunciado**

Configura el indicador con [PALEO] seguido de la ruta y el signo de cierre. Esta condición se comprueba en el entorno real. Después escribe COMPROBAR.

**Desarrollo**

```bat
PROMPT [PALEO] $P$G
COMPROBAR
```

**Qué comprueba**

- PROMPT debe ser `[PALEO] $P$G` en el entorno real.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.

### Etapa 7 de 12

**Enunciado**

Comprueba dónde busca programas la consola sin modificar esa lista. Identifica el separador. Después escribe COMPROBAR.

**Desarrollo**

```bat
PATH
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Comando de consulta:»: `PATH`.
- Respuesta a «Separador:»: `;`.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.

### Etapa 8 de 12

**Enunciado**

Consulta la etiqueta y serie del volumen. Diseña, sin ejecutarla, la orden que pondría FOSILES a un USB E: previamente identificado. Después escribe COMPROBAR.

**Desarrollo**

```bat
VOL
LABEL /?
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Consulta de etiqueta y serie:»: `VOL`.
- Respuesta a «Cambio propuesto para el USB:»: `LABEL E: FOSILES`.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.

### Etapa 9 de 12

**Enunciado**

Las cámaras necesitan diagnóstico de C: sin reparación. Propón la orden como texto e identifica la opción que NO debes añadir si solo consultas. Después escribe COMPROBAR.

**Desarrollo**

```bat
CHKDSK /?
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Diagnóstico:»: `CHKDSK C:`.
- Respuesta a «Opción de reparación que omites:»: `/F`.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.

### Etapa 10 de 12

**Enunciado**

Abre otra consola para la torre con título Torre Paleo y consulta de versión, dejándola abierta. Ciérrala con EXIT y vuelve a esta actividad. Después escribe COMPROBAR.

**Desarrollo**

```bat
START "Torre Paleo" CMD /K VER
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Orden para abrirla:»: `START "Torre Paleo" CMD /K VER`.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.

### Etapa 11 de 12

**Enunciado**

Elabora el plan de cierre: apagado en 60 segundos y cancelación si llega una visita tardía. Responde como texto, sin ejecutar el plan. Después escribe COMPROBAR.

**Desarrollo**

```bat
SHUTDOWN /?
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Apagado programado:»: `shutdown /s /t 60`.
- Respuesta a «Cancelación:»: `shutdown /a`.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.

### Etapa 12 de 12

**Enunciado**

Entrega el turno: sal con EXIT y vuelve a esta misión desde el menú. Restablece el indicador [PALEO] con ruta y signo de cierre y comprueba el final. Después escribe COMPROBAR.

**Desarrollo**

```bat
EXIT
REM Vuelve a la actividad 12 / Itzuli 12. jarduerara
PROMPT [PALEO] $P$G
COMPROBAR
```

**Qué comprueba**

- Debe abrirse otra sesión tras superar el paso anterior. Se pide EXIT; MENU también permite superar esta condición.
- PROMPT debe ser `[PALEO] $P$G` en el entorno real.

Primera pista: Consulta la ayuda y observa qué información necesita el equipo del parque.


## Juego 13 Extra — El examen de los guardas del parque

Los guardas te describen una herramienta y tú identificas el comando. Contesta dentro de COMPROBAR; no ejecutes la respuesta.

Comandos: CHKDSK, CLS, CMD, COLOR, DATE, EXIT, HELP, LABEL, PATH, PROMPT, SHUTDOWN, SYSTEMINFO, START, TIME, TITLE, VER, VOL.

### Etapa 1 de 17

**Enunciado**

Comprueba el sistema de archivos de un volumen. Responde solo el nombre del comando. Después escribe COMPROBAR.

**Desarrollo**

```bat
REM Respuesta / Erantzuna: CHKDSK
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Comando:»: `CHKDSK`.

Primera pista: Primera letra: C

### Etapa 2 de 17

**Enunciado**

Limpia la pantalla de la consola. Responde solo el nombre del comando. Después escribe COMPROBAR.

**Desarrollo**

```bat
REM Respuesta / Erantzuna: CLS
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Comando:»: `CLS`.

Primera pista: Primera letra: C

### Etapa 3 de 17

**Enunciado**

Inicia el intérprete de comandos de Windows. Responde solo el nombre del comando. Después escribe COMPROBAR.

**Desarrollo**

```bat
REM Respuesta / Erantzuna: CMD
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Comando:»: `CMD`.

Primera pista: Primera letra: C

### Etapa 4 de 17

**Enunciado**

Cambia los colores de texto y fondo de la consola. Responde solo el nombre del comando. Después escribe COMPROBAR.

**Desarrollo**

```bat
REM Respuesta / Erantzuna: COLOR
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Comando:»: `COLOR`.

Primera pista: Primera letra: C

### Etapa 5 de 17

**Enunciado**

Consulta o establece la fecha del sistema. Responde solo el nombre del comando. Después escribe COMPROBAR.

**Desarrollo**

```bat
REM Respuesta / Erantzuna: DATE
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Comando:»: `DATE`.

Primera pista: Primera letra: D

### Etapa 6 de 17

**Enunciado**

Sale del intérprete actual. Responde solo el nombre del comando. Después escribe COMPROBAR.

**Desarrollo**

```bat
REM Respuesta / Erantzuna: EXIT
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Comando:»: `EXIT`.

Primera pista: Primera letra: E

### Etapa 7 de 17

**Enunciado**

Muestra la ayuda de los comandos. Responde solo el nombre del comando. Después escribe COMPROBAR.

**Desarrollo**

```bat
REM Respuesta / Erantzuna: HELP
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Comando:»: `HELP`.

Primera pista: Primera letra: H

### Etapa 8 de 17

**Enunciado**

Permite cambiar la etiqueta de un volumen. Responde solo el nombre del comando. Después escribe COMPROBAR.

**Desarrollo**

```bat
REM Respuesta / Erantzuna: LABEL
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Comando:»: `LABEL`.

Primera pista: Primera letra: L

### Etapa 9 de 17

**Enunciado**

Consulta o establece la lista de rutas de búsqueda de ejecutables. Responde solo el nombre del comando. Después escribe COMPROBAR.

**Desarrollo**

```bat
REM Respuesta / Erantzuna: PATH
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Comando:»: `PATH`.

Primera pista: Primera letra: P

### Etapa 10 de 17

**Enunciado**

Personaliza el indicador donde se escriben órdenes. Responde solo el nombre del comando. Después escribe COMPROBAR.

**Desarrollo**

```bat
REM Respuesta / Erantzuna: PROMPT
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Comando:»: `PROMPT`.

Primera pista: Primera letra: P

### Etapa 11 de 17

**Enunciado**

Gestiona el apagado del sistema. Responde solo el nombre del comando. Después escribe COMPROBAR.

**Desarrollo**

```bat
REM Respuesta / Erantzuna: SHUTDOWN
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Comando:»: `SHUTDOWN`.

Primera pista: Primera letra: S

### Etapa 12 de 17

**Enunciado**

Muestra información detallada del equipo y del sistema. Responde solo el nombre del comando. Después escribe COMPROBAR.

**Desarrollo**

```bat
REM Respuesta / Erantzuna: SYSTEMINFO
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Comando:»: `SYSTEMINFO`.

Primera pista: Primera letra: S

### Etapa 13 de 17

**Enunciado**

Abre otra ventana para ejecutar un programa u orden. Responde solo el nombre del comando. Después escribe COMPROBAR.

**Desarrollo**

```bat
REM Respuesta / Erantzuna: START
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Comando:»: `START`.

Primera pista: Primera letra: S

### Etapa 14 de 17

**Enunciado**

Consulta o establece la hora del sistema. Responde solo el nombre del comando. Después escribe COMPROBAR.

**Desarrollo**

```bat
REM Respuesta / Erantzuna: TIME
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Comando:»: `TIME`.

Primera pista: Primera letra: T

### Etapa 15 de 17

**Enunciado**

Cambia el título de la ventana de comandos. Responde solo el nombre del comando. Después escribe COMPROBAR.

**Desarrollo**

```bat
REM Respuesta / Erantzuna: TITLE
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Comando:»: `TITLE`.

Primera pista: Primera letra: T

### Etapa 16 de 17

**Enunciado**

Muestra la versión de Windows. Responde solo el nombre del comando. Después escribe COMPROBAR.

**Desarrollo**

```bat
REM Respuesta / Erantzuna: VER
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Comando:»: `VER`.

Primera pista: Primera letra: V

### Etapa 17 de 17

**Enunciado**

Muestra la etiqueta y el número de serie del volumen. Responde solo el nombre del comando. Después escribe COMPROBAR.

**Desarrollo**

```bat
REM Respuesta / Erantzuna: VOL
COMPROBAR
```

**Qué comprueba**

- Respuesta a «Comando:»: `VOL`.

Primera pista: Primera letra: V

## Dudas frecuentes

- COMPROBAR no existe fuera del juego: entra en una actividad desde jugar.bat.
- La ruta de programas ha cambiado: no sustituyas PATH. Sal al menú y vuelve a entrar.
- La respuesta de fecha falla: consulta DATE /T de nuevo y copia toda la salida.
- SYSTEMINFO tarda: espera a que termine; copia solo el nombre del equipo cuando se solicite.
- El título no cambia en la pestaña: revisa la configuración de la aplicación de terminal; el motor no lo valida automáticamente.
- COLOR deja de verse después de COMPROBAR: la interfaz tiene colores propios; revisa el resultado justo después de COLOR.
- El PROMPT no coincide: reproduce el patrón con $P y $G. La personalización se pierde al salir; vuelve a establecerla.
- START interpreta el título como ruta: el primer texto entre comillas es el título de la nueva ventana.
- CHKDSK requiere permisos: se trabaja aparte con el profesor, no elevando el juego.
- No se permite anclar un acceso: documenta la limitación de la versión o de las políticas de Windows.
- Sigue apareciendo la edición anterior: REINICIAR carga el nuevo JSON, previa confirmación y borrado solo de esa actividad.
- Cambiar idioma no reinicia: traduce interfaz y enunciados, conservando progreso.

## Actividades supervisadas

La ficha PRACTICAS_SUPERVISADAS.md recoge accesos directos, USB y consulta del disco. No se sustituyen por scripts. Apagado y cancelación reales requieren guardar antes el trabajo de la VM.

## Fuentes

- 3.2- Intro de Windows en comandos.pdf, aportado por el docente.
- 3.2.1- Actividades de Windows en comandos.odt, aportado por el docente.
- Documentación Microsoft Learn: https://learn.microsoft.com/windows-server/administration/windows-commands/windows-commands

## Validación

19 pruebas de lógica superadas en Linux, con consultas del sistema simuladas. La prueba adicional con CMD real está incluida y pendiente de ejecutar en Windows. No confundir la validación lógica con la prueba completa de la VM.
