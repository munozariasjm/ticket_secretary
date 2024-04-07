# Class for sending emails

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Email:
    def __init__(self, email, subject, body):
        self.email = email
        self.subject = subject
        self.body = body

    def send(self):

        email = self.email
        password = "password"
        subject = self.subject
        message = self.body

        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = email
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        text = msg.as_string()
        server.sendmail(email, email, text)
        server.quit()

        print("Email sent successfully")