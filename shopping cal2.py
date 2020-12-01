import speech_recognition as sr
from gtts import gTTS
import playsound
import sympy as sp
from sympy import *
import webbrowser
import os

#Audio
r = sr.Recognizer()
m = sr.Microphone()

#threhold
with m as a source: r.adjust_for_ambient_noise(source)
print('set the minimum source to ()'.format(r.energy_threshold))

def checkspeech(r):
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        print('คุณพูดว่า :' , r.recognize_google(audio , language = 'th-TH') )
    except sr.UnknownValueError:
        print('ไม่ได้ยินเสียงของคุณ')
        return ('WW')
    except sr.RequestError:
        print('ไม่สามารถเข้าถึงข้อมูลจาก Google ได้')
        return ('WW')


run = True
while run == True:
    with m as source: r.adjust_for_ambient_noise(source)
    print('set the minimum source to ()'.format(r.energy_threshold))
    print('มีอะไรให้ช่วยไหมครับ')

    speech = str(checkspeech(r))
    if speech == 'สายเปย์' or 'saipay' or 'สายเป':

        print('สายเปย์มาแล้วครับ')


#Main code ค่อยแก้ไข

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