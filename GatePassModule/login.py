import os
import sqlite3
from tkinter import *
from tkinter import messagebox


class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1350x700+0+0')
        self.root.title('Login Page')
        self.root.config(bg='white')

        # =============Log in Frame
        Login_Frame = Frame(self.root, bd=4, relief=RIDGE, bg='green')
        Login_Frame.place(x=360, y=90, width=350, height=460)
        Label(Login_Frame, text='Login to the system', font=('times new roman', 20, 'bold'), bg='#262626',
              fg='white').pack(side=TOP, fill=X)

        Label(Login_Frame, text='Emp. ID: ', font=('times new roman', 20), bg='lightgrey').place(x=2, y=100)
        self.employeeid = StringVar()
        self.password = StringVar()

        Entry(Login_Frame, textvariable=self.employeeid, font=('times new roman', 15)).place(x=140,
                                                                                             y=102,
                                                                                             width=170,
                                                                                             height=32)

        Label(Login_Frame, text='Password: ', font=('times new roman', 20), bg='lightgrey').place(x=2, y=150)
        Entry(Login_Frame, textvariable=self.password, show='*', font=('times new roman', 15)).place(x=140,
                                                                                                     y=152,
                                                                                                     width=170,
                                                                                                     height=32)
        Button(Login_Frame, text='Log In', command=self.login, font=('times new roman', 15, 'bold'),
               bg='red', fg='white').place(x=190, y=210, width=100, height=25)

    def login(self):
        con = sqlite3.connect(database=r'../ims.db')
        cur = con.cursor()
        try:
            if self.employeeid.get() == "" or self.password.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                eid = self.employeeid.get();
                pwd = self.password.get();
                cur.execute('select utype, eid, name from employee where eid = ? AND pass = ?',
                            (eid, pwd))
                user = cur.fetchone()
                if user == None:
                    messagebox.showerror("Error", "Invalid USERNAME/PASSWORD", parent=self.root)
                else:
                    if user[0] == 'GUARD':
                        self.root.destroy()
                        os.system("python dashboard_guard.py {} {} {}".format("GUARD", user[1], user[2]))
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : str{(ex)}", parent=self.root)


root = Tk()
obj = Login_System(root)
root.mainloop()
