import speech_recognition as sr
import sympy as sp
from sympy import *
import webbrowser
import googlesearch 
from gtts import gTTS
import playsound
import os

#jum function
jum_list = []

while True:

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("พูดอะไรบางอย่างสิ... :")
        audio = r.listen(source)
        text = r.recognize_google(audio , language = 'th-TH')

        if 'จำ' in text:
            jum_num = text.strip('จำ')
            jum_list.append(int(jum_num))
            print(jum_num)
            print('ราคาสินค้าทั้งหมดที่จำ : ', jum_list )

        elif text == 'รวม':
            print('ผลรวมจากการใช้ฟังก์ชันรวม : ' , str(sum(jum_list)))
            

        elif text == 'ปิดโปรแกรม' or text == 'ปิด' or text == 'หยุด':
            print('ปิดโปรแกรม')
            break

        elif 'สินค้า' in text:
            word_shopee = text.strip('สินค้า')
            print('Shopee Search!')
            webbrowser.open('https://shopee.co.th/' + word_shopee)


        else:
            text = r.recognize_google(audio , language = 'th-TH')
            result = simplify(text)
            print("คุณพูดว่า : {}".format(text))
            print('ผลลัพท์ของคุณคือ :' , result)
    