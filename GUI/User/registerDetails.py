from tkinter import *
from tkinter import messagebox, filedialog
import pyrebase

from Email.process import emailProcess

class SecondForm:
    def detailsForm(self):
        ws = Tk()
        ws.title('Register Details')
        ws.config(bg='#0B5A81')


        # main_frame = Frame(ws)
        # main_frame.pack(fill=BOTH, expand=1)
        # my_canvas=Canvas(main_frame)
        # my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        # my_scrollbar = tkinter.Scrollbar(main_frame, VERTICAL, command=my_canvas.yview)
        # my_scrollbar.pack(side=RIGHT, fill=Y, expand=1)
        # my_scrollbar.configure(yscrollcommand = my_scrollbar.set)
        # my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scollregion = my_canvas.bbox("all")))

        # second_frame = Frame(my_canvas)
        # my_canvas.create_window((0,0),window = second_frame, anchor="nw")


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


        def submitDetails():
            username = register_username.get()
            aadhaar_no = register_aadhaar.get()
            name = register_name.get()
            gender = var.get()
            yob = register_yob.get()
            mobile = register_mobile.get()
            state = variable.get()
            address = register_address.get("1.0", END)
            data = {
                "aadhaar_no" : aadhaar_no,
                "name" : name,
                "gender" : gender,
                "yob" : yob,
                "mobile" : mobile,
                "state" : state,
                "address" : address
            }
            if not db.child(username).shallow().get().val():
                print("users does not exist")
                messagebox.showinfo("Error Occurred!", "Oops! The user does not exist.\nEnter a valid username")
            else:
                print("users exist")
                db.child(username).child("details").set(data)
                emailID = db.child(username).child("Email").get()
                print(emailID.val())
                subject = "Details submission successful!"
                message = "Congratulations! " + username + "\nYou have successfully submitted your Aadhaar Details to our system."\
                                                           "\nRest assured. Your details are in good hands. We will keep it safe."\
                                                            "\nReagrds,\nTeam AutoKYC."
                messagebox.showinfo("Submission Successful!", "You will receive "
                                                                "communication shortly on your registered Email ID.")
                emailProcess.send_mail(emailID.val(), subject, message)
                ws.destroy()


        f = ('Times', 14)
        var = StringVar()
        var.set('male')

        stateList = []
        variable = StringVar()
        states = open('D:\\SPIT\\Semester 4\\Mini Project\\Wroking Module\\VerifyMe\\GUI\\User\\states.txt', 'r')
        for state in states:
            state = state.rstrip('\n')
            stateList.append(state)
        variable.set(stateList[0])

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
            text="Aadhaar Number",
            bg='#CCCCCC',
            font=f
        ).grid(row=1, column=0, sticky=W, pady=10)

        Label(
            right_frame,
            text="Enter Name",
            bg='#CCCCCC',
            font=f
        ).grid(row=2, column=0, sticky=W, pady=10)

        Label(
            right_frame,
            text="Select Gender",
            bg='#CCCCCC',
            font=f
        ).grid(row=3, column=0, sticky=W, pady=10)

        Label(
            right_frame,
            text="Select YOB",
            bg='#CCCCCC',
            font=f
        ).grid(row=4, column=0, sticky=W, pady=10)

        Label(
            right_frame,
            text="Contact Number",
            bg='#CCCCCC',
            font=f
        ).grid(row=5, column=0, sticky=W, pady=10)


        Label(
            right_frame,
            text="Select State",
            bg='#CCCCCC',
            font=f
        ).grid(row=6, column=0, sticky=W, pady=10)

        Label(
            right_frame,
            text="Enter Address",
            bg='#CCCCCC',
            font=f
        ).grid(row=7, column=0, sticky=W, pady=10)

        Label(
            right_frame,
            text="Username",
            bg='#CCCCCC',
            font=f
        ).grid(row=8, column=0, sticky=W, pady=10)

        gender_frame = LabelFrame(
            right_frame,
            bg='#CCCCCC',
            padx=10,
            pady=10,
        )

        register_aadhaar = Entry(
            right_frame,
            font = f
        )

        register_name = Entry(
            right_frame,
            font=f
        )

        register_mobile = Entry(
            right_frame,
            font=f
        )

        male_rb = Radiobutton(
            gender_frame,
            text='Male',
            bg='#CCCCCC',
            variable=var,
            value='M',
            font=('Times', 10),

        )

        female_rb = Radiobutton(
            gender_frame,
            text='Female',
            bg='#CCCCCC',
            variable=var,
            value='F',
            font=('Times', 10),

        )

        others_rb = Radiobutton(
            gender_frame,
            text='Others',
            bg='#CCCCCC',
            variable=var,
            value='O',
            font=('Times', 10)

        )

        register_yob = Entry(
            right_frame,
            font=f
        )

        register_state = OptionMenu(
            right_frame,
            variable,
            *stateList)

        register_state.config(
            width=15,
            font=('Times', 12)
        )
        register_address = Text(
            right_frame,
            font=f,
            width=20,
            height=3
        )

        register_username = Entry(
            right_frame,
            font=f
        )


        register_btn = Button(
            right_frame,
            width=15,
            text='Register',
            font=f,
            relief=SOLID,
            cursor='hand2',
            command=submitDetails
        )

        register_aadhaar.grid(row=1, column=1, pady=10, padx=20)
        register_name.grid(row=2, column=1, pady=10, padx=20)
        gender_frame.grid(row=3, column=1, pady=10, padx=20)
        male_rb.pack(expand=True, side=LEFT)
        female_rb.pack(expand=True, side=LEFT)
        others_rb.pack(expand=True, side=LEFT)
        register_yob.grid(row=4, column=1, pady=10, padx=20)
        register_mobile.grid(row=5, column=1, pady=10, padx=20)
        register_state.grid(row=6, column=1, pady=10, padx=20)
        register_address.grid(row=7, column=1, pady=10, padx=20)
        register_username.grid(row=8, column=1, pady=10, padx=20)
        register_btn.grid(row=12, column=1, pady=10, padx=20)
        right_frame.pack()


        ws.mainloop()
