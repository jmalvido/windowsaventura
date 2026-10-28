# Piloto en la máquina virtual

La lógica se ha comprobado en Linux. Falta validar la interacción en Windows.

1. Ejecuta jugar.bat desde una ruta con espacios.
2. Ejecuta py -3 -m unittest discover -s tests -v. En Windows no debe omitirse la prueba CMD.
3. Completa juegos 1 y 3; prueba PISTA, AYUDA y REINICIAR.
4. Usa MENU desde una subcarpeta y vuelve. Debe recuperar la carpeta.
5. SALIR, abre de nuevo y comprueba archivos y pasos guardados.
6. En el juego 5 establece el PROMPT solicitado y compruébalo.
7. En el 6 comprueba VER, DATE /T y SYSTEMINFO reales.
8. En el 7 guarda VOL sin elevar el juego ni ejecutar reparaciones.
9. En el 8 prueba START, EXIT y reentrada.
10. En el 10 ejecuta los .bat y comprueba que CALL regresa al primero.
11. Completa la misión final y comprueba el expediente al volver a entrar.
12. Cambia a euskera y reinicia una actividad de prueba. Las demás deben conservarse.
13. Una vez publicado el repo, prueba el actualizador con un archivo de alumno.
    Debe conservarlo y crear copia anterior; con el menú abierto debe rechazarlo.

Si algo falla, copia el mensaje completo, juego, paso, VER y py -3 --version.
Las teclas Tab y flechas, el título, los colores y las acciones gráficas se revisan
visualmente. No se interceptan todas las órdenes. Es una práctica, no un examen protegido.
