# Importamos sys pal try
import sys, subprocess

# Funcion pa instalar las librerias
def install_libraries():
    for lib in ["SpeechRecognition", "googletrans==4.0.0-rc1", "tkinter"]:
        try:
            __import__(lib.split("==")[0])
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

# Intentamos instalar las librerias si se necesita
install_libraries()

## Librerias para reconocer la voz
import speech_recognition as sr
# Librerias para traducir
from googletrans import Translator
## Libreria para desplegar ventanas
from tkinter import Tk, filedialog

## Definimos función para automatizar la transcripción del audio
def transcripcion(wav, txt): # Le pasamos el archivo wav
    # Inicializar el reconocedor
    r = sr.Recognizer()
    # Abrir el archivo de audio
    with sr.AudioFile(wav) as source:
        # Reemplazarlo con el archivo
        audio = r.record(source)
        # Intentar reconocer la voz (se especifica el lenguaje)
        texto = r.recognize_google(audio, language="ja-JP")
        # Crear un .txt que contenga el texto en la ruta especificada
        with open(txt, 'w', encoding='utf-8') as f:
            f.write(texto)
    print("Transcripción completada y guardada")

## Traducir el archivo (le pasamos la ruta donde guardaremos)
def traduccion(txt, trad): # Le pasamos el txt de la transcripcion
    # Pasamos la ruta
    with open(txt, 'r', encoding='utf-8') as f:
                texto = f.read()
                # Iniciar el traductor
                translator = Translator()
                # Traducir el texto
                traduccion = translator.translate(texto, src="ja", dest="en")
                # Se crea el archivo en la ruta que se guardará
                with open(trad, 'w', encoding='utf-8') as g:
                    g.write(traduccion.text) #se usa el .text para usar solo la cadena de texto
    print("Traducción completada y guardada")

## Definimos función para que automatice el proceso
def tran_y_trad():
    # Abrir la ventana
    Tk().withdraw()
    # Seleccionamos el archivo .wav
    wav = filedialog.askopenfilename(title = "Selecciona el archivo .wav",
                                            filetypes = [("Archivo .wav", "*.wav")])
    if not wav:
         print("No se seleccionó archivo")
    # Guardamos ruta para la transcripcion
    txt = filedialog.asksaveasfilename(title = "Guardar transcripcion .txt",
                                       defaultextension=".txt",
                                       filetypes=[("Archivos de texto", "*.txt")])
    if not txt:
         print("No se seleccionó archivo")
    # Guardamos ruta para la traduccion
    trad = filedialog.asksaveasfilename(title = "Guardar traduccion .txt",
                                        defaultextension=".txt",
                                        filetypes=[("Archivos de texto", "*.txt")])
    if not trad:
         print("No se seleccionó archivo")
    # Usamos las funciones anteriores para realizar el proceso
    transcripcion(wav, txt)
    traduccion(txt, trad)
    print("Proceso completado")

## Ahora llamamos a la función y rezo que funcione
tran_y_trad()