# Piloto de Paleo Isla en Windows

La lógica se ha probado en Linux; falta verificar CMD real en la VM.

1. Ejecuta jugar.bat desde una ruta con espacios.
2. Ejecuta py -3 -m unittest discover -s tests -v. La prueba CMD no debe omitirse.
3. Completa las tres primeras misiones, usando PISTA y AYUDA.
4. Sal con SALIR, vuelve y comprueba el progreso guardado.
5. Revisa PROMPT [TRICERATOPS] $P$G en la misión 3.
6. Comprueba SYSTEMINFO y el nombre real de equipo en la misión 4.
7. Prueba la nueva ventana con START y la reentrada con EXIT en la misión 9.
8. Responde el plan de apagado como texto, sin ejecutarlo, en la misión 10.
9. Completa la reapertura final: al volver, restablece PROMPT [PALEO] $P$G.
10. Cambia a euskera y comprueba textos y pistas.
11. Si tenías actividades 0.1 empezadas, reinicia una y verifica que carga dinosaurios
    sin alterar las demás. Prueba también cancelar el reinicio.
12. Publicado el repo, prueba el actualizador con datos existentes; deben conservarse.

Guarda mensaje completo, juego, paso, salida de VER y versión de Python si hay errores.
Colores, título, teclas y tareas gráficas requieren revisión visual.
