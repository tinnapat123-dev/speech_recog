import datetime
import speech_recognition as sr
import pyautogui as pg
import os
import time

r = sr.Recognizer()
m = sr.Microphone()

with m as source: r.adjust_for_ambient_noise(source)
print('set the minimum energy threshold to', r.energy_threshold)

def checkspeech(r):
    with sr.Microphone() as source:
        audio = r.listen(source)

    try: 
        print('You said: ', r.recognize_google(audio))
        return (r.recognize_google(audio))

    except sr.UnknownValueError:
        print('Error condition')
        return ('WW')

    except sr.RequestError as e:
        print('Could not request the result from Google')
        return ('WW')

def main():
    
    run = True

    while run:
        with m as source: r.adjust_for_ambient_noise(source)
        print('Set the Minimun Threshold to' , r.energy_threshold)
        print('Welcome to the powerpoint assistant!! Say sth.... ')

        speech = str(checkspeech(r))

        if speech == 'Next':
            pg.press('right')

        elif speech == 'back':
            pg.press('left')

main()
