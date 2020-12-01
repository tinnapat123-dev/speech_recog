import speech_recognition as sr
import sympy as sp
from sympy import *
import webbrowser

jum_list = []


while True:

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)

        if 'jum' in text:
            jum_num = text.strip('jum')
            jum_list.append(jum_num)
            print(jum_num)

        elif text == 'รวม':
            print('ผลรวมจากการใช้ฟังก์ชันรวม : ' + str(sum(jum_list)))
            
        elif sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            
        elif sr.RequestError:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

        elif text == 'ปิดโปรแกรม' or text == 'ปิด' or text == 'หยุด':
            print('ปิดโปรแกรม')
            break

        else:
            text = r.recognize_google(audio , language = 'th-TH')
            result = simplify(text)
            print("คุณพูดว่า : {}".format(text))
            print('ผลลัพท์ของคุณคือ :' , result)
            
        


        
