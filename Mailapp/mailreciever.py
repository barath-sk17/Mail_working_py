import os
import matplotlib.pyplot as plt
from collections import Counter
import imaplib
import email
import dateutil.parser
from datetime import datetime
import matplotlib.pyplot as plt
from collections import Counter

from email.header import Header,decode_header,make_header

# Connect to the Gmail IMAP server
imap_server = imaplib.IMAP4_SSL('imap.gmail.com')


EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

# Log in to your Gmail account
email_address = EMAIL_ADDRESS
password = EMAIL_PASSWORD
imap_server.login(email_address, password)

# Select the inbox folder
imap_server.select('inbox')

#only for the text message maily only


# Fetch a list of all message IDs in the inbox
#result, message_ids = imap_server.search(None, 'ALL')
#message_ids_list = message_ids[0].split()

# Print the list of message IDs
# print('List of message IDs:')
# for message_id in message_ids_list:
#     print(message_id.decode())

#status, messages = imap_server.search(None, 'FROM', 'baraththinker@gmail.com')
Dataset=[]
status, messages = imap_server.search(None,'ALL')

# iterate through messages
for msg_num in messages[0].split():
    # fetch the email message by ID
    status, email_data = imap_server.fetch(msg_num, "(RFC822)")
    
    #print(email_data)
    
    email_msg = email.message_from_bytes(email_data[0][1]) 
    
    
    print(f"Message Number : {msg_num}")
    print(f"From : {email_msg.get('From')}")
    print(f"To : {email_msg.get('To')}")
    print(f"BCC : {email_msg.get('BCC')}")
    print(f"Date : {email_msg.get('Date')}")
    print(f"Subject : {email_msg.get('Subject')}")
    print("Content : ")
    for part in email_msg.walk():
        if part.get_content_type() == "text/plain":
            print(part.as_string())
    
    Dataset.append(email_msg.get('Date'))
    
    
    # decode the email message into a readable format
    # raw_email = email_data[0][1].decode("utf-8")
    # email_message = email.message_from_string(raw_email)

    # # print subject and sender
    # print("Subject:", decode_header(email_message["Subject"])[0][0])
    # print("From:", decode_header(email_message["From"])[0][0])

# Log out of the IMAP server
imap_server.logout()
formatted_data=[]

print("\n\n\n",Dataset)

for date_str in Dataset:
    try:
        # Try to parse the date string using datetime.strptime()
        dt = datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S %z")
    except ValueError:
        # If the above fails, use dateutil.parser.parse()
        dt = dateutil.parser.parse(date_str)
    formatted_data.append(dt.strftime("%d %b"))
#print(formatted_data)



#data = ['13 Mar', '21 Mar', '21 Mar', '21 Mar', '21 Mar', '21 Mar', '22 Mar', '22 Mar', '22 Mar', '25 Mar', '29 Mar', '29 Mar', '29 Mar', '29 Mar', '30 Mar']
counts = Counter(formatted_data)

x = list(counts.keys())
y = list(counts.values())

plt.bar(x, y)
plt.xlabel('Time and Month')
plt.ylabel('Frequency')
plt.show()

# Display plot
plt.show()


# import imaplib
# import email



# imap_server = "imap.gmail.com"
# email_address = EMAIL_ADDRESS
# password=EMAIL_PASSWORD


# imap = imaplib.IMAP4_SSL(imap_server)
# imap.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

# imap.select("Inbox")