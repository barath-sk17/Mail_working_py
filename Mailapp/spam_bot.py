import os
import smtplib, ssl
import text_bot

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

def sendEmail(message):
    smtp_server = "smtp.gmail.com"
    port=587
    sender_email = EMAIL_ADDRESS
    password = EMAIL_PASSWORD
    receiver_mail="21pc28@psgtech.ac.in"
    
    context = ssl.create_default_context()
    
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email,password)
        server.sendmail(sender_email,receiver_mail,message)
        
    except Exception as e:
        print(e)
     
    finally:
        server.quit()
        

print("\n\t     Type of mail : ")
print("\n\t 1 Working Professional")
print("\t 2 Student")
ch=int(input("\n\t Typ your Choice : "))

if(ch==1):
    txt = text_bot.text1
    sendEmail(txt)
elif(ch==2):
    txt = text_bot.text2
    sendEmail(txt)      
    
     