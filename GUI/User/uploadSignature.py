import os.path
from tkinter import *
import pyrebase
from PIL import ImageTk, Image
from tkinter import filedialog, messagebox
from Email.process import emailProcess
from Email.mailAttachment import emailAttachment
from GenerateQRPackage import generateQR


class FifthForm:
    def uploadSignatureForm(self):
        ws = Tk()
        ws.title('Upload Signature')
        ws.config(bg='#0B5A81')

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
        storage = firebase.storage()
        db = firebase.database()
        auth = firebase.auth()

        f = ('Times', 14)

        def browse_signature():
            global my_image
            Label(
                right_frame,
                text="Location",
                bg='#CCCCCC',
                font=f
            ).grid(row=2, column=0, sticky=W, pady=10)

            filename = filedialog.askopenfilename(
                title="Upload Signature",
                filetypes=(("PNG Files", "*.png"), ("JPEG Files", "*.jpg"), ("All Files", "*.*"))
            )

            Label(
                right_frame,
                text=filename,
                bg='#CCCCCC',
                font=f
            ).grid(row=2, column=1, sticky=W, pady=10)

            def upload_signature():
                username = register_username.get()
                if not db.child(username).shallow().get().val():
                    print("users does not exist")
                    messagebox.showinfo("Error Occurred!", "Oops! The user does not exist.\nEnter a valid username")
                else:
                    print("users exist")
                    emailID = db.child(username).child("Email").get()
                    path_on_cloud = username + "/signature.png"
                    path_on_local = filename
                    storage.child(path_on_cloud).put(path_on_local)

                    # uploading to storage directory
                    email = "verifyme.communications@gmail.com"
                    password = "verify_me@password"
                    user = auth.sign_in_with_email_and_password(email, password)
                    print(user)
                    image_url = storage.child(username).child("signature.png").get_url(user['idToken'])
                    print("this is signature url: ", image_url)
                    db.child(username).child("signature_url").set(image_url)
                    subject = "Signature has been uploaded."
                    message = "Congratulations! " + username + ",\nYou have successfully uploaded your signature to " \
                                                               "our server.\nRegards,\nTeam AutoKYC "
                    messagebox.showinfo("Upload Successful!", "Signature submission Successful!\nYou will receive "
                                                              "communication shortly on your registered Email ID."
                                                              "\nThank You!")
                    emailProcess.send_mail(emailID.val(), subject, message)
                    ws.destroy()
                    generateQR.generateQRClass.generateQRMethod(username)
                    receiver_mail = db.child(username).child("Email").get().val()
                    emailAttachment.mailImage(receiver_mail)

            Label(
                right_frame,
                text="Preview",
                bg='#CCCCCC',
                font=f
            ).grid(row=3, column=0, sticky=W, pady=10)

            og_pic = Image.open(filename)
            resized = og_pic.resize((555, 394), Image.ANTIALIAS)
            my_image = ImageTk.PhotoImage(resized)
            my_image_label = Label(
                right_frame,
                image=my_image
            ).grid(row=3, column=1, sticky=W, pady=10)

            register_btn = Button(
                right_frame,
                width=15,
                text='Upload',
                font=f,
                relief=SOLID,
                cursor='hand2',
                command=upload_signature
            )

            register_btn.grid(row=4, column=1, pady=10, padx=20)

        right_frame = Frame(
            ws,
            bd=2,
            bg='#CCCCCC',
            relief=SOLID,
            padx=10,
            pady=10
        )

        Label(
            right_frame,
            text="Username",
            bg='#CCCCCC',
            font=f
        ).grid(row=0, column=0, sticky=W, pady=10)

        register_username = Entry(
            right_frame,
            font=f
        )
        register_username.grid(row=0, column=1, pady=10, padx=20)

        browse_button_label = Label(
            right_frame,
            text="Upload Profile Picture",
            bg='#CCCCCC',
            font=f,
        ).grid(row=1, column=0, sticky=W, pady=10)

        browse_btn = Button(
            right_frame,
            width=15,
            text='Browse',
            font=f,
            relief=SOLID,
            cursor='hand2',
            command=browse_signature
        )
        browse_btn.grid(row=1, column=1, pady=10, padx=20)

        right_frame.pack()

        ws.mainloop()
