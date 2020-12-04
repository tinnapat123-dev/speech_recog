import speech_recognition as sr
import pyautogui as pg

while True:

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speech Powerpoint Command... :")
        audio = r.listen(source)
        text = r.recognize_google(audio , language='en-EN')

        if text == 'next':
            pg.press('right')

        elif text == 'back':
            pg.press('left')

        elif text == 'presentation':
            pg.click(1151 , 716)
            pg.click(1151 , 716)

        elif text == 'white':
            pg.press('w')

        elif text == 'finish':
            pg.press('esc')
            print('Command End!! Nice Presentation!!')
            break

            

       