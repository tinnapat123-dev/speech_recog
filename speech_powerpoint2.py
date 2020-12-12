import speech_recognition as sr
import time
from subprocess import call
import pyautogui as pg


r = sr.Recognizer()

print("Beginning to listen...")

def listen():
        with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
        try:
                return r.recognize_google(audio , language='th-TH')

        except sr.UnknownValueError:
                print("Could not understand audio")
                
        return ""

print("Trying to always listen...")

while 1:
        if listen() == 'ต่อไป':
            pg.press('right')
            print('Right')

        elif listen() == 'ย้อน':
            pg.press('left')
            print('Left')

        elif listen() == 'จบการนำเสนอ':
            pg.press('esc')
            break

        elif listen() == 'สวัสดี':
            pg.press('spacebar')
              