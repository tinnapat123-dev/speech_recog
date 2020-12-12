import speech_recognition as sr
import pyautogui as pg


while True:

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speech Powerpoint Command... :")
        audio = r.listen(source)
        text = r.recognize_google(audio , language='th-TH')
        
        if text == 'ต่อไป':
            pg.press('right')

        elif text == 'ย้อน':
            pg.press('left')

        elif text == 'เริ่ม':
            pg.click(1151 , 716)
            pg.click(1151 , 716)

        elif text == 'สีขาว':
            pg.press('w')

        elif text == 'จบการนำเสนอ':
            pg.press('esc')
            print('Command End!! Nice Presentation!!')
            break

        elif text == sr.UnknownValueError:
            print("I do not understand the words")
            continue

        

        


            

       