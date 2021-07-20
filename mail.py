import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Email:
    def __init__(self):
        self.sender_email_id = 'kamvelihle.buka2907@gmail.com'
        self.receiver_email_id = ['kamvaelihle@gmail.com', 'retshepilekoloko27@gmail.com', 'mpendulokhozamk2@gmail.com', 'ayamzazi@gmail.com.com']
        self.password = input("Enter your password: ")
        self.subject = "Greetings"
        self.msg = MIMEMultipart()
        self.msg['From'] = self.sender_email_id
        self.msg['To'] = ', ' .join(self.receiver_email_id)
        self.msg['Subject'] = self.subject
        self.body = "hey\n"

        self.msg.attach(MIMEText(self.body, 'plain'))

        self.text = self.msg.as_string()
        self.s = smtplib.SMTP('smtp.gmail.com', 587)
        # start TLS for security
        self.s.starttls()
# Authentication

        self.s.login(self.sender_email_id, self.password)
# message to be sent

# sending the mail
        self.s.sendmail(self.sender_email_id, self.receiver_email_id, self.text)
# terminating the session
        self.s.quit()
