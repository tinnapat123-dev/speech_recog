import time
import speech_recognition as sr

def callback(recognizer , audio):
    print(recognizer.recognize_google(audio))

recognizer = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    recognizer.adjust_for_ambient_noise(source)

stop_listenning = recognizer.listen_in_background(mic , callback)
stop_listenning(wait_for_stop = False)