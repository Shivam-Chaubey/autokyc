import smtplib
import os


# class emailProcess:
#     def send_mail(recepient, message):
#         server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
#         sender = "verifyme.communications@gmail.com"
#         password = "verify_me@password"
#         server.login(sender, password)
#         # receiver = "shivamspit@gmail.com"
#         server.sendmail(sender, str(recepient), str(message))
#         server.quit()


import smtplib
from email.message import EmailMessage


class emailProcess:
    def send_mail(recepient, subject, message):
        email_id = "verifyme.communications@gmail.com"
        email_pass = "verify_me@password"

        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = email_id
        msg['To'] = recepient
        msg.set_content(message)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_id,email_pass)
            smtp.send_message(msg)