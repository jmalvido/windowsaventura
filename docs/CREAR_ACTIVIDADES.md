# Añadir actividades

Copia un JSON y asigna actividad_014, etc. El archivo debe llamarse como su id.
No se edita el menú. Mantén schema 1 y motor_minimo 1; incrementa version al corregir.
Incluye es y eu en título, final, archivos, textos y pistas. Añade solucion_docente.
Las rutas internas usan /; los enunciados usan la barra invertida escapada en JSON.

Pruebas: respuesta, carpeta, contenido, ausente, vacio, respuesta_sistema, salida,
entorno, texto y reentrada. contenido compara con un archivo inicial admitiendo CRLF/LF.
texto compara las líneas no vacías en orden, ignorando caja y espacios; no ejecuta .bat.
salida compara con consultas de lectura predefinidas; nunca ejecuta texto del JSON.
entorno comprueba PROMPT o PATH heredados. reentrada compara la sesión con la del
último paso superado. Las pruebas conceptuales no certifican ejecución.

Las consultas nuevas requieren ampliar retos.py y sus pruebas. Los escenarios iniciados
conservan su definición hasta REINICIAR.

Antes de publicar, prueba en Windows, ejecuta los tests y py -3 publicar_catalogo.py.
Sube los JSON y catálogo. Si cambias el motor, usa el actualizador completo externo.
