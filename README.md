# Traductor
Convertidor Speech-to-Text de audios en japonés a inglés para su posterior traducción (v2.2).
Se usa la libreria "speech_recognition" para la transcripción del audio en japonés a un archivo txt, en este punto, es necesario que el audio esté en formato .wav.
Se usa la libreria "googletrans" para la traducción del texto transcrito en japonés a inglés.
O puedes usar la version de la libreria de "Deepl" (Preferiblemente con una Api personal) (Limitado a 50,000 chr/mes)

## Cambios
- Se implementaron funciones para cada paso (Transcripción y Traducción)
- Se implementó una función para seleccionar las rutas para seleecionar los archivos
- Se automatizó el proceso junto con prints que indican el progreso
- Se agregó la función de instalar las librerias automaticamente
- Ahora se puede usar DeepL como traductor otorgandole una key, se trabaja en implementarlo con el codigo en general

## Requisitos
- googletrans 4.0.0
- speech_recognition 3.8.1
- tkinter
- DeepL (De usar la version de deepl)
