#python -m smtpd -c DebuggingServer -n localhost:1025
import os
import smtplib

#for importing image for the sake of attachement in the mail
import imghdr

from email.message import EmailMessage


from FileChooserScript import choose_file
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')


#multiple user
#contacts = ['practicemail93@gmail.com','baraththinker@gmail.com','vishalram676@gmail.com']
#contacts = ['practicemail93@gmail.com','baraththinker@gmail.com']
contacts = ['21pc28@psgtech.ac.in'] #['21pc32@psgtech.ac.in']
#contacts = ['practicemail93@gmail.com']

#multiple image
# image_file=['quote.jpg','alan.jpg']
#-----image_file=choose_file()


#organised way of sending message
msg = EmailMessage()
msg['Subject']="You just Cracked it!!"
msg['From']=EMAIL_ADDRESS
msg['To']=",".join(contacts)
msg.set_content("I'm jut glad that , this is my first networks project and I'm happy to say, Salam Bhai")

response1=input("\n Do you like to add Image file : ")

if (response1 == "yes" or response1 == "Yes"):
    image_file=choose_file()
    
    if len(image_file)!=0:
        for image in image_file:
            with open(image,'rb') as f:
                
        #with open('quote.jpg','rb') as f:  # for opening single image file
                
                file_data = f.read()
                print(file_data)
                file_type = imghdr.what(f.name) 
                file_name = f.name
                print(file_name)
                
                #print(file_type)
            
            msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
            #msg.add_attachment(file_data,maintype='image',subtype=file_type,filename=file_name)
            
    else:
        print('''You are facing some issue the ".img" -- file is not attached to the corresponding gmail !!''')
    


response2=input("\n Do you like to add Pdf file : ")

if (response2 == "yes" or response2 == "Yes"):
    pdf_file=choose_file()
    
    if (len(pdf_file)!=0):
    #sending pdf file
        #with open("mail.pdf",'rb') as pdf:
        for pdftraversal in pdf_file:
            with open(pdftraversal,'rb') as pdf: 
                pdf_data = pdf.read()
                
                pdf_name = pdf.name
                
        msg.add_attachment(pdf_data,maintype="application",subtype="octet-stream",filename=pdf_name)
    
    else:
        print('''You are facing some issue the ".pdf" --file is not attached to the corresponding gmail !!''')
    
    
    
#print(EMAIL_ADDRESS, EMAIL_PASSWORD)

#just normal mail port but  smtp.ehlo(),smtp.starttls(),smtp.ehlo() need to be added
#with smtplib.SMTP('smtp.gmail.com',587) as smtp: 

    
#with smtplib.SMTP('localhost',1025) as smtp:   #to check the program in localhost
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp :
     #smtp.ehlo()
     #smtp.starttls()
     #smtp.ehlo()
    
     smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)


     #unorganised way of sending message
     
     #subject = 'Email Sender bruh !!'
     #body = 'Just for the practice session'
     #msg = f'Subject : {subject}\n\n{body}'
     #smtp.sendmail(EMAIL_ADDRESS,'practicemail93@gmail.com', msg)
     
     #organised way of sending message
     smtp.send_message(msg)