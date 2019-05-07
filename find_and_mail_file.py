#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 10:05:25 2019

@author: MCA
"""


import smtplib, ssl

from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

import os,sys
import time

def loadFiles(subdir, filetype):
    """
    example:
    dirs = ["dir1", "dir2"]
    file_type = ".dat"
    files, keys, data = loadFiles(dirs[0], file_type)
    
    """    
    
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, (subdir+"/"))
    files_path = []
    fileNamesFiltered = []
    for root, dirs, files in os.walk(path):  
        for i, filename in enumerate(files):
            if filename[(len(filename))-len(filetype):] == filetype:
#                print(filename)
                filename_path = path + filename
                files_path.append(filename_path)
                fileNamesFiltered.append(filename)
                  
    
    return fileNamesFiltered



def sendMail(filename):
    smtp_server = "smtp.seznam.cz"
    port = 25  # For starttls
    sender_email = "xxx@email.cz"
    #password = input("Type your password and press enter: ")
    password = "xxxx"
    
    # Create a secure SSL context
    context = ssl.create_default_context()
    receiver_email=sender_email
    
    
    #compose an email
    message = MIMEMultipart("alternative")
    message["Subject"] = ("analysis status check: "+ str(filename))
    message["From"] = sender_email
    message["To"] = receiver_email
    
    text = "analysis status check"
    part1 = MIMEText(text, "plain")
    message.attach(part1)
    
    
    #send file
#    filename = file
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
        print("logged in")
        # TODO: Send email here
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("mail sent")
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit() 


#--------------------------------------------------------------------------------------
if __name__ == "__main__":

    run = True
    directory = "/folder/folder"
    fileType = ".xxx"
    name = "xxxxxx_xxx__xxx.xxx"
    
    while run == True:
        
        names = loadFiles(directory, fileType)
        print("running")
        if name in names:
         print("file found:", name)
         f = open(name, "r")
         for line in f:
            if "THE ANALYSIS HAS" in line: 
                sendMail(name)
                print("file sent")
                run = False
                print("done")
                sys.exit()
        time.sleep(300)
