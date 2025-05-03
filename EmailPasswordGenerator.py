#send an email using python 
#steps :
# go over gmail and set up 2 factor authentication 
# generate app password 
# create a function to send an email 


from email.message import EmailMessage
from app2 import password
import ssl 
import smtplib


email_sender = "codewithmansi@gmail.com"
email_password = "your_app_password" # use the app password generated from your google account
email_receiver = ''
subject = "dont forget to subscribe to my channel"
body = """  

Hello, this is a test email sent from Python!
I hope you are doing well. This is a test email to check the functionality of sending emails using Python.  
I hope you find this information helpful. If you have any questions or need further assistance, feel free to reach out.
Thank you for your time and have a great day!   
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

