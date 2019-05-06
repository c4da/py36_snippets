#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: MCA
"""


import email, smtplib, ssl

from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

smtp_server = "smtp.seznam.cz"
port = 25  # For starttls
sender_email = "xxxx@xxx.xx"
#password = input("Type your password and press enter: ")
password = "xxxxxx"

# Create a secure SSL context
context = ssl.create_default_context()
receiver_email=sender_email


#compose an email
message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email

text = "321"
part1 = MIMEText(text, "plain")
message.attach(part1)


#send file
filename = "file.txt"
try:
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        file = MIMEBase("application", "octet-stream")
        file.set_payload(attachment.read())
        encoders.encode_base64(file)
        file.add_header(
                            "Content-Disposition",
                            f"attachment; filename= {filename}",
                        )
        message.attach(file)
except:
    print("file not found")

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    # TODO: Send email here
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("mail sent")
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit() 
