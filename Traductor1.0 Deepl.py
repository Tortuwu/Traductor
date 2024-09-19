#importamos sys pal try
import sys, subprocess

# Funcion pa intalar las librerias
def install_libraries():
    for lib in ["SpeechRecognition", "tkinter", "deepl"]:
        try:
            __import__(lib.split("==")[0])
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

# Intentamos instalar las librerias si se necesita
install_libraries()
#Importamos el speech recognition, el traductor y la ventana para selecionar los archivos
import speech_recognition as sr
from tkinter import Tk, filedialog
import deepl

#Definimos estas variales, de idioma de destino y Api de Deepl

target_lang = "EN-US"  # Definimos el idioma EN-US EN-GB
auth_key = "1ae19495-2b6a-4827-9e32-1ae6fa98a313:fx" #Api de Deepl

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
def traduccion(txt, trad, target_lang, auth_key):#Le pasamos el txt de la transcripcion
    
    translator = deepl.Translator(auth_key) #Definimos la funcion de traducir

    # Definimos la ruta
    with open(txt, "r", encoding="utf-8") as file:
        text = file.read()

    # Traducimos
    try:
        traduccion = translator.translate_text(text, target_lang=target_lang)

        # Escribimos el output en el archivo txt
        with open(trad, "w", encoding="utf-8") as file:
            file.write(traduccion.text)
    except Exception as e:
        print(f"Error durante la traducción: {e}")

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
    traduccion(txt, trad, target_lang, auth_key)
    print("Proceso completado")

## Ahora llamamos a la función y rezo que funcione
tran_y_trad()