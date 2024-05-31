import speech_recognition as sr
import pyttsx3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web_driver import Info


# obtain audio from the microphone
recognizer = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 180)
engine.setProperty('voice', voices[1].id)




def speak(text):
    engine.say(text)
    engine.runAndWait()




with sr.Microphone() as source:
    recognizer.energy_threshold = 1000
    recognizer.adjust_for_ambient_noise(source, 1.2)
    speak("Hello, i'm your voice assistant, how can  i help you ?")
    print("Listening...")
    audio = recognizer.listen(source)
    try:
        #convert the audio to text
        command = recognizer.recognize_google(audio)
        print("You said: " + command)
    except sr.UnknownValueError:
        print("Sorry, I could not understand audio")
    except sr.RequestError as e:
        print("Error; {0}".format(e))
if "what" and "about" and "you" in command:
    speak("I'm having a good day, thank you.")
speak("How can i help you ?")


with sr.Microphone() as source:
    recognizer.energy_threshold = 1000
    recognizer.adjust_for_ambient_noise(source, 1.2)
    print("Listening...")
    audio = recognizer.listen(source)
    command2 = recognizer.recognize_google(audio)

info = ""
if "information" in command2:
    speak("You need information related to which topic ?")
    with sr.Microphone() as source:
        recognizer.energy_threshold = 1000
        recognizer.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = recognizer.listen(source)
        info = recognizer.recognize_google(audio)
        



assistant = Info()
response = assistant.get_info(info)
speak(response)

