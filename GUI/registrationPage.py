import sqlite3
from tkinter import *

root = Tk()
root.title("Registration Page")
root.geometry("400x400");

conn = sqlite3.connect('user.db')

c = conn.cursor()

# c.execute("drop table registration")
# c.execute("drop table login")
# c.execute("drop table data")
# c.execute("""CREATE TABLE registration(
#                 username text,
#                 f_name text,
#                 m_name text,
#                 l_name text,
#                 gender text,
#                 father text,
#                 mother text,
#                 flatbuilding text,
#                 landmark text,
#                 area text,
#                 road text,
#                 city text,
#                 districtpin text,
#                 state text,
#                 email text,
#                 mobile integer
#             )""")
#
# c.execute("CREATE TABLE login(username text, password text)")
#
# c.execute("CREATE TABLE data(username text, aadhar blob, image blob, sign blob)")

username_label = Label(root, text="Username")
username_label.grid(row=0, column=0, padx=20)
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=1, column=0, padx=20)
m_name_label = Label(root, text="Middle Name")
m_name_label.grid(row=2, column=0, padx=20)
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=3, column=0, padx=20)
gender_label = Label(root, text="Gender")
gender_label.grid(row=4, column=0, padx=20)
father_label = Label(root, text="Father's Name")
father_label.grid(row=5, column=0, padx=20)
mother_label = Label(root, text="Mother's Name")
mother_label.grid(row=6, column=0, padx=20)
flat_no_label = Label(root, text="Flat-Building")
flat_no_label.grid(row=7, column=0, padx=20)
landmark_label = Label(root, text="Landmark")
landmark_label.grid(row=8, column=0, padx=20)
area_label = Label(root, text="Area")
area_label.grid(row=9, column=0, padx=20)
street_label = Label(root, text="Street")
street_label.grid(row=10, column=0, padx=20)
city_label = Label(root, text="City")
city_label.grid(row=11, column=0, padx=20)
district_label = Label(root, text="District - PIN")
district_label.grid(row=12, column=0, padx=20)
state_label = Label(root, text="State")
state_label.grid(row=13, column=0, padx=20)
email_label = Label(root, text="Email ID")
email_label.grid(row=14, column=0, padx=20)
mobile_label = Label(root, text="Mobile Number")
mobile_label.grid(row=15, column=0, padx=20)

username_edit = Entry(root, width=30)
username_edit.grid(row=0, column=1, padx=20, columnspan=2)
f_name_edit = Entry(root, width=30)
f_name_edit.grid(row=1, column=1, padx=20, columnspan=2)
m_name_edit = Entry(root, width=30)
m_name_edit.grid(row=2, column=1, padx=20, columnspan=2)
l_name_edit = Entry(root, width=30)
l_name_edit.grid(row=3, column=1, padx=20, columnspan=2)
var = StringVar()
Radiobutton(root, text='Male', variable=var, value="Male").grid(row=4, column=1)
Radiobutton(root, text="Female", variable=var, value="Female").grid(row=4, column=2)
father_edit = Entry(root, width=30)
father_edit.grid(row=5, column=1, padx=20, columnspan=2)
mother_edit = Entry(root, width=30)
mother_edit.grid(row=6, column=1, padx=20, columnspan=2)
flat_no_edit = Entry(root, width=30)
flat_no_edit.grid(row=7, column=1, padx=20, columnspan=2)
landmark_edit = Entry(root, width=30)
landmark_edit.grid(row=8, column=1, padx=20, columnspan=2)
area_edit = Entry(root, width=30)
area_edit.grid(row=9, column=1, padx=20, columnspan=2)
street_edit = Entry(root, width=30)
street_edit.grid(row=10, column=1, padx=20, columnspan=2)
city_edit = Entry(root, width=30)
city_edit.grid(row=11, column=1, padx=20, columnspan=2)
district_edit = Entry(root, width=30)
district_edit.grid(row=12, column=1, padx=20, columnspan=2)
state_edit = Entry(root, width=30)
state_edit.grid(row=13, column=1, padx=20, columnspan=2)
email_edit = Entry(root, width=30)
email_edit.grid(row=14, column=1, padx=20, columnspan=2)
mobile_edit = Entry(root, width=30)
mobile_edit.grid(row=15, column=1, padx=20, columnspan=2)


# Continue here
def submit():
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute(
        "INSERT INTO registration VALUES (:username,:gender,:f_name,:m_name,:l_name,:father,:mother,:flatbuilding,:landmark,:area,:street,:city,:districtpin,:statename,:email,:mobile)",
        {
            'username': username_edit.get(),
            'f_name': f_name_edit.get(),
            'm_name': m_name_edit.get(),
            'l_name': l_name_edit.get(),
            'gender': var.get(),
            'father': father_edit.get(),
            'mother': mother_edit.get(),
            'flatbuilding': flat_no_edit.get(),
            'landmark': landmark_edit.get(),
            'area': area_edit.get(),
            'street': street_edit.get(),
            'city': city_edit.get(),
            'districtpin': district_edit.get(),
            'statename': state_edit.get(),
            'email': email_edit.get(),
            'mobile': mobile_edit.get()
        })
    conn.commit()
    conn.close()

    username_edit.delete(0, END)
    f_name_edit.delete(0, END)
    m_name_edit.delete(0, END)
    l_name_edit.delete(0, END)
    father_edit.delete(0, END)
    mother_edit.delete(0, END)
    flat_no_edit.delete(0, END)
    landmark_edit.delete(0, END)
    area_edit.delete(0, END)
    street_edit.delete(0, END)
    city_edit.delete(0, END)
    district_edit.delete(0, END)
    state_edit.delete(0, END)
    email_edit.delete(0, END)
    mobile_edit.delete(0, END)


submit_button = Button(root, text="Submit", command=submit)
submit_button.grid(row=16, column=0, pady=10, columnspan=2, padx=10, ipadx=50)


def resettext():
    username_edit.delete(0, END)
    f_name_edit.delete(0, END)
    m_name_edit.delete(0, END)
    l_name_edit.delete(0, END)
    father_edit.delete(0, END)
    mother_edit.delete(0, END)
    flat_no_edit.delete(0, END)
    landmark_edit.delete(0, END)
    area_edit.delete(0, END)
    street_edit.delete(0, END)
    city_edit.delete(0, END)
    district_edit.delete(0, END)
    state_edit.delete(0, END)
    email_edit.delete(0, END)
    mobile_edit.delete(0, END)


reset_button = Button(root, text="Reset", command=resettext)
reset_button.grid(row=16, column=1, pady=10, columnspan=2, padx=10, ipadx=50)


# Query to check if inserted
def checktable():
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute("SELECT *,oid FROM registration ")
    records = c.fetchall()
    # c.fetchone()
    # c.fetchmany(50)
    print(records)
    print_records = ''
    for record in records:
        print_records += str(record) + "\n"
    query_label = Label(root, text=print_records)
    query_label.grid(row=18, column=0, columnspan=3)
    conn.commit()
    conn.close()


query_button = Button(root, text="Check", command=checktable)
query_button.grid(row=17, column=0, pady=10, padx=10, columnspan=2, ipadx=100)

conn.commit()
conn.close()

root.mainloop()
