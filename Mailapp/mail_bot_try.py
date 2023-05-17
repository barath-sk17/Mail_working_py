import os
import smtplib
import speech_recognition as sr
import pyttsx3

import gtts  
from playsound import playsound  


listener = sr.Recognizer()


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    

def get_info():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Talk")
            audio_text = r.listen(source)
            print("Time over, thanks")
        try:
            text = r.recognize_google(audio_text)
            return text
        except:
            return "Unable to understand"
    except:
        return "Voice not captured"


    # try:
    #     with sr.Microphone() as source:
    #         print('listening ...')
    #         listener.adjust_for_ambient_noise(source, duration=5)
    #         voice = listener.listen(source)
    #         try:
    #             info = listener.recognize_google(voice)
    #             print(info.lower())
    #             return info.lower()   
    #         except:
    #             print("sorry")
    #         #return info.lower()
            
    # except:
    #     pass

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    
    EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
    EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    
    
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    
    server.sendmail(EMAIL_ADDRESS,'practicemail93@gmail.com','mail-bot :) ucdkuudsvuvbsfuvbfbvfuvfbvbfuvbudfvufdvbufdvdfubdfubvbufvbufvbufvbufbuvfubvfuvubdfvf')
    server.se

def get_email_info():
    count=0
    while(count<=2):
        if(count==0):
            speak('To Whom you want to send email')
            person = get_info()
        elif(count==1):
            speak('What is the subject of your email ? ')
            subject = get_info()
        elif(count==2):
            speak('Tell me your text in your email')
            body = get_info()
        count+=1
    print(person, subject, body)
    
    
get_email_info()