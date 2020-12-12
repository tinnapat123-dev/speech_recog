import speech_recognition as sr
import pyautogui as pg


while True:

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speech Powerpoint Command... :")
        audio = r.listen(source)
        text = r.recognize_google(audio , language='th-TH')
        
        try:

            if 'ต่อไป' in text:
                pg.press('right')

            elif 'ย้อน' in text:
                pg.press('left')

            elif text == 'จบการนำเสนอ':
                pg.press('esc')
                print('Command End!! Nice Presentation!!')
                break

        except sr.UnknownValueError:
            print("I do not understand the words")
            continue
