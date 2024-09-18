## Librerias para reconocer la voz
import speech_recognition as sr

## Archivo a transcribir
# Seleccionar el archivo
archivo = "C:/Users/Mcuin/Desktop/Otros/Traducciones/audio.wav"

## Inicializar el reconocedor
r = sr.Recognizer()

# Abrir el archivo de audio
with sr.AudioFile(archivo) as source:
    # Reemplazarlo con el archivo
    audio = r.record(source)
    # Intentar reconocer la voz (se especifica el lenguaje)
    texto = r.recognize_google(audio, language="ja-JP")
    # Crear un .txt que contenga el texto en la ruta especificada
    with open('C:/Users/Mcuin/Desktop/Otros/Traducciones/transcripcion.txt', 'w', encoding='utf-8') as f:
        f.write(texto)

## Traducir el archivo
# Librerias para traducir
from googletrans import Translator

# Seleccionar el archivo a traducir
# Se usa de esta manera porque no pude incluirlo dentro del with anterior por el tipo de variable
# que se creaba
with open("C:/Users/Mcuin/Desktop/Otros/Traducciones/transcripcion.txt", 'r', encoding='utf-8') as f:
            texto = f.read()
            # Iniciar el traductor
            translator = Translator()
            # Traducir el texto
            traduccion = translator.translate(texto, src="ja", dest="en")
            # Se crea el archivo en la ruta que se guardará
            with open('C:/Users/Mcuin/Desktop/Otros/Traducciones/traduccion.txt', 'w', encoding='utf-8') as g:
                g.write(traduccion.text) #se usa el .text para usar solo la cadena de texto
