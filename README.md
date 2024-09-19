# Traductor
Convertidor Speech-to-Text de audios en japonés a inglés para su posterior traducción (v1.0).
Se usa la libreria "speech_recognition" para la transcripción del audio en japonés a un archivo txt, en este punto, es necesario que el audio esté en formato .wav.
Se usa la libreria "googletrans" para la traducción del texto transcrito en japonés a inglés.
O puedes usar la version de la libreria de "Deepl" (Preferiblemente con una Api personal)

## Cambios
- Se implementaron funciones para cada paso (Transcripción y Traducción)
- Se implementó una función para seleccionar las rutas para seleecionar los archivos
- Se automatizó el proceso junto con prints que indican el progreso
- Se agregó la función de instalar las librerias automaticamente

## Requisitos
- googletrans 4.0.0
- speech_recognition 3.8.1
- tkinter
- Deepl (De usar la version de deepl)
