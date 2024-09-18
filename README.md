# Traductor
Convertidor Speech-to-Text de audios en japonés a inglés para su posterior traducción (v1.0).
Se usa la libreria "speech_recognition" para la transcripción del audio en japonés a un archivo txt, en este punto, es necesario que el audio esté en formato .wav.
Se usa la libreria "googletrans" para la traducción del texto transcrito en japonés a inglés.

## Cambios
- Se implementaron funciones para cada paso (Transcripción y Traducción)
- Se implementó una función para seleccionar las rutas para seleecionar los archivos
- Se automatizó el proceso junto con prints que indican el progreso