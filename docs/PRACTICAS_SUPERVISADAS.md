# Prácticas que revisa el profesor

Complemento de los juegos 7 y 9, basado en la hoja aportada. El corrector comprueba
respuestas conceptuales; no certifica la realización de estas operaciones.

## Accesos directos

1. Escritorio → Nuevo → Acceso directo. Destino cmd.exe; nombre Simbolo del sistema.
2. Crea Apagar 60 con destino:
   shutdown.exe /s /t 60 /c "El equipo se apagará en un minuto"
3. En Propiedades → Cambiar icono, selecciona un icono de Windows.
4. Crea Apagar con destino: shutdown.exe /s /t 20 /c "Apagando..."
5. Crea No apagar con destino: shutdown.exe /a
   La palabra «anuncie» de la hoja se interpreta como «anule» el apagado.
6. Cambia el icono de Apagar por un símbolo de apagado disponible.
7. Revisa las opciones de anclar al Inicio o a la barra de tareas. Su disponibilidad
   depende de Windows, el tipo de acceso y las políticas del centro. Si no están
   disponibles, documenta la limitación sin cambiar políticas.
8. El profesor revisa destinos, nombres e iconos sin ejecutar el apagado.

No sustituyas los accesos directos por scripts. Para demostrar cancelación, guarda
todo el trabajo de la VM, programa 60 segundos y usa inmediatamente shutdown /a.
Con /t mayor que cero, Windows implica cierre forzado de aplicaciones: no hagas
la demostración con documentos sin guardar. Capturas: propiedades y cancelación.

## Etiqueta de un USB

Consulta VOL C: sin cambiar el sistema. Si hay un USB de prácticas, confirma primero
su letra en el Explorador. Usa VOL X:, LABEL X: APELLIDO y de nuevo VOL X:.
Sustituye X: por la letra verificada. Sin USB, documenta la sintaxis sin utilizar otra unidad.

## CHKDSK

Sal del juego. Abre otro CMD como administrador y ejecuta CHKDSK C: si C: es el volumen
acordado. No añadas /F, /R ni /X: se pide información, no reparación. Interpreta con
el profesor el informe del volumen activo. Documenta el resultado y sal con EXIT.
No se eleva todo el juego.

## Documentación de referencia

- https://learn.microsoft.com/windows-server/administration/windows-commands/shutdown
- https://learn.microsoft.com/windows-server/administration/windows-commands/chkdsk
- https://learn.microsoft.com/windows-server/administration/windows-commands/label
