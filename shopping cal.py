import speech_recognition as sr
from gtts import gTTS
import playsound
import sympy as sp
from sympy import *
import webbrowser

r = sr.Recognizer()

x, y = symbols(['x', 'y'])
system = [Eq(3*x + 4*y, 7) , Eq(5*x + 6*y, 8)]
soln = solve(system, [x, y])

jum = []



with sr.Microphone() as source:
    while True:
        print('...ยินดีต้อนรับสู่ SHOPPING CAL พูดอะไรซักหน่อย...')
        audio = r.listen(source)
        text = r.recognize_google(audio,language = "th-TH")

        #text = r.recognize_google(audio,language = "th-TH")
    
        if text == 'ลาซาด้า' or text == 'lazada':
            print('Lazada Open!')
            webbrowser.open('https://www.lazada.com')
            
        elif text == 'ช้อปปี้' or text ==  'ช็อปปี้' or text ==  'shopee' or text == 'shoppy':
            print('Shopee Open!')
            webbrowser.open('https://www.shopee.com')

        elif text == 'หยุด':
            print('Stop Application')
            break

        elif text == 'จำ' + text:
            jum.append(text)
            print(jum)

        else:
            operationed_result = simplify(text)
            print('สมการของคุณ : ',text)
            print('คำตอบของคุณ : ',operationed_result)
            
            
            
            
    
        #hear = gTTS(text,lang='th')
        #hear.save('speech_beta1.mp3')
        #playsound.playsound('speech beta1',True)