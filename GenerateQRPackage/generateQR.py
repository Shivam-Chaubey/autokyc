import qrcode
import pyrebase

# class generateQRClass:
#     def generateQRMethod("testuser"):
configFirebaseDB = {
    "apiKey": "AIzaSyAD3wPlVrio_guYW8Q51Sq9E3erYp2ialY",
    "authDomain": "autokyc-97b29.firebaseapp.com",
    "databaseURL": "https://autokyc-97b29-default-rtdb.firebaseio.com",
    "projectId": "autokyc-97b29",
    "storageBucket": "autokyc-97b29.appspot.com",
    "messagingSenderId": "610795330604",
    "appId": "1:610795330604:web:146b3c0fab0c0248460589",
    "measurementId": "G-L6BQP0D34D"
}
firebase = pyrebase.initialize_app(configFirebaseDB)
db = firebase.database()

email_id = db.child("testuser").child("Email").get().val()
aadhaar_url = db.child("testuser").child("aadhaar_url").get().val()
proile_url = db.child("testuser").child("profile_url").get().val()
signature_url = db.child("testuser").child("signature_url").get().val()

aadhaar_no = db.child("testuser").child("details").child("aadhaar_no").get().val()
address = db.child("testuser").child("details").child("address").get().val()
gender = db.child("testuser").child("details").child("gender").get().val()
mobile = db.child("testuser").child("details").child("mobile").get().val()
name = db.child("testuser").child("details").child("name").get().val()
state = db.child("testuser").child("details").child("state").get().val()
yob = db.child("testuser").child("details").child("yob").get().val()

qr_data = f"Aadhaar Card Number: {aadhaar_no}\nName: {name}\nGender: {gender}\nYear of Birth: {yob}" \
          f"\nEmail: {email_id}\nContact Number: {mobile}\nAddress: {address}\nState: {state}"
qr_url_aadhar = f"Aadhar Card: {aadhaar_url}"
qr_url_profile = f"Profile Photo: {proile_url}"
qr_url_signature = f"Signature: {signature_url}"
qr_code = qrcode.make(qr_data)
qr_code_aadhaar_url = qrcode.make(qr_url_aadhar)
qr_code_profile_url = qrcode.make(qr_url_profile)
qr_code_signature_url = qrcode.make(qr_url_signature)
qr_code.save("D:\\SPIT\\Semester 4\\Mini Project\\Wroking Module\\VerifyMe\\Email\\user_data.png")
qr_code_aadhaar_url.save("D:\\SPIT\\Semester 4\\Mini Project\\Wroking Module\\VerifyMe\\Email\\aadhar_url.png")
qr_code_profile_url.save("D:\\SPIT\\Semester 4\\Mini Project\\Wroking Module\\VerifyMe\\Email\\profile_url.png")
qr_code_signature_url.save("D:\\SPIT\\Semester 4\\Mini Project\\Wroking Module\\VerifyMe\\Email\\signature_url.png")
