import smtplib
import imghdr
from email.message import EmailMessage

class emailAttachment:
    def mailImage(mail_id):
        email_id = "verifyme.communications@gmail.com"
        email_pass = "verify_me@password"

        msg = EmailMessage()
        msg['Subject'] = "Thank You for your co-operation"
        msg['From'] = email_id
        msg['To'] = mail_id
        msg.set_content("You have successfully completed your process.\nPFA QR Codes for your data.\nProfile Data = user_data.png\nAadhar Card URL = aadhar_url.png\nProfile Photo = profile_url.png\nSignature = signature_url.png")
        with open('D:\\SPIT\\Semester 4\\Mini Project\\Wroking Module\\VerifyMe\\Email\\user_data.png', 'rb') as m:
            file_data = m.read()
            user_file_type = imghdr.what(m.name)
            user_file_name = m.name

        msg.add_attachment(file_data, maintype='image', subtype = user_file_type, filename = user_file_name)

        with open('D:\\SPIT\\Semester 4\\Mini Project\\Wroking Module\\VerifyMe\\Email\\aadhar_url.png', 'rb') as m:
            file_data = m.read()
            aadhaar_file_type = imghdr.what(m.name)
            aadhaar_file_name = m.name

        msg.add_attachment(file_data, maintype='image', subtype = aadhaar_file_type, filename = aadhaar_file_name)

        with open('D:\\SPIT\\Semester 4\\Mini Project\\Wroking Module\\VerifyMe\\Email\\profile_url.png', 'rb') as m:
            file_data = m.read()
            profile_file_type = imghdr.what(m.name)
            profile_file_name = m.name

        msg.add_attachment(file_data, maintype='image', subtype = profile_file_type, filename = profile_file_name)

        with open('D:\\SPIT\\Semester 4\\Mini Project\\Wroking Module\\VerifyMe\\Email\\signature_url.png', 'rb') as m:
            file_data = m.read()
            signature_file_type = imghdr.what(m.name)
            signature_file_name = m.name

        msg.add_attachment(file_data, maintype='image', subtype = signature_file_type, filename = signature_file_name)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_id,email_pass)
            smtp.send_message(msg)
            print("Thank you............")