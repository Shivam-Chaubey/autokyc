from tkinter import *
from tkinter import messagebox

import cv2
import pyrebase
from Email.process import emailProcess


class FirstForm:
    def credentialsForm(test):
        ws = Tk()
        ws.title('Register Credentials')
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
        db = firebase.database()

        def submitInitial():
            username = register_username.get()
            emailID = register_email.get()
            password = register_pwd.get()
            confirmPassword = pwd_again.get()
            data = {
                "Email": emailID,
                "Password": password
            }
            if password == confirmPassword:
                docName = str(username)
                db.child(docName).set(data)
                subject = "Welcome Onboard!"
                message = "Congratulations! " + username + ",\nYou have been successfully registered with the " \
                                                           "AutoKYC. We hope that you have a swift process ahead.\n"\
                                                            "Regards,\nTeam AutoKYC"
                messagebox.showinfo("Registration Successful!", "Congratulations! Welcome aboard. \n You will receive "
                                                                "communication shortly on your registered Email ID.")
                emailProcess.send_mail(emailID, subject, message)
                ws.destroy()
            else:
                messagebox.showerror("Password Mismatch!", "Entered passwords do not match.")
                register_pwd.delete(0, END)
                pwd_again.delete(0, END)

        f = ('Times', 14)
        var = StringVar()
        var.set('male')

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
            text="Enter Username",
            bg='#CCCCCC',
            font=f
        ).grid(row=0, column=0, sticky=W, pady=10)

        Label(
            right_frame,
            text="Enter Email",
            bg='#CCCCCC',
            font=f
        ).grid(row=1, column=0, sticky=W, pady=10)
        Label(
            right_frame,
            text="Enter Password",
            bg='#CCCCCC',
            font=f
        ).grid(row=2, column=0, sticky=W, pady=10)
        Label(
            right_frame,
            text="Re-enter Password",
            bg='#CCCCCC',
            font=f
        ).grid(row=3, column=0, sticky=W, pady=10)

        register_username = Entry(
            right_frame,
            font=f
        )

        register_email = Entry(
            right_frame,
            font=f
        )
        register_pwd = Entry(
            right_frame,
            font=f,
            show='*'
        )
        pwd_again = Entry(
            right_frame,
            font=f,
            show='*'
        )

        register_btn = Button(
            right_frame,
            width=15,
            text='Register',
            font=f,
            relief=SOLID,
            cursor='hand2',
            command=submitInitial
        )

        register_username.grid(row=0, column=1, pady=10, padx=20)
        register_email.grid(row=1, column=1, pady=10, padx=20)
        register_pwd.grid(row=2, column=1, pady=10, padx=20)
        pwd_again.grid(row=3, column=1, pady=10, padx=20)
        register_btn.grid(row=4, column=1, pady=10, padx=20)
        right_frame.pack()

        ws.mainloop()
