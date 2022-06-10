import os
import sqlite3
import tkinter.font
from tkinter import *
from tkinter import messagebox


class NewGatePass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1350x700+0+0')
        self.root.title('New Gate Pass')
        self.root.config(bg='white')

        self.database_name = r'../ims.db'
        self.visitor_name = StringVar()
        self.visitor_contact = StringVar()
        self.visitor_address = StringVar()
        self.visitor_vehicle = StringVar()

        new_gate_pass_frame = Frame(self.root, bd=4, relief=RIDGE, bg='green')
        new_gate_pass_frame.place(x=360, y=90, width=350, height=460)

        font = tkinter.font.Font(name='times new roman', size=16)
        label_title = Label(new_gate_pass_frame, text='New Gate Pass', font=font, bg='#262626', fg='white').pack(
            side=TOP, fill=X)
        lbl_visitor_name = Label(new_gate_pass_frame, text='Visitor Name: ', font=font,
                                 bg='lightgrey').place(x=2, y=100)
        txt_visitor_name = Entry(new_gate_pass_frame, textvariable=self.visitor_name,
                                 font=font).place(x=140, y=102, width=170, height=32)

        lbl_visitor_contact = Label(new_gate_pass_frame, text='Visitor Contact: ', font=font, bg='lightgrey').place(x=2,
                                                                                                                    y=150)
        txt_visitor_contact = Entry(new_gate_pass_frame, textvariable=self.visitor_contact,
                                    font=font).place(x=140, y=152, width=170, height=32)

        lbl_visitor_address = Label(new_gate_pass_frame, text='Visitor Address: ', font=font, bg='lightgrey').place(x=2,
                                                                                                                    y=200)
        txt_visitor_address = Entry(new_gate_pass_frame, textvariable=self.visitor_address,
                                    font=font).place(x=140, y=202, width=170, height=32)

        lbl_visitor_contact = Label(new_gate_pass_frame, text='Visitor Vehicle: ', font=font, bg='lightgrey').place(x=2,
                                                                                                                    y=250)
        txt_visitor_contact = Entry(new_gate_pass_frame, textvariable=self.visitor_vehicle,
                                    font=font).place(x=140, y=252, width=170, height=32)

        btn_create = Button(new_gate_pass_frame, text='Create', command=self.create_gate_pass,
                            font=font,
                            bg='red', fg='white').place(x=190, y=302, width=100, height=25)

    def create_gate_pass(self):
        print('create_gate_pass')
        con = sqlite3.connect(database=self.database_name)
        cur = con.cursor()
        try:
            if self.visitor_name.get() == "" or self.visitor_contact.get() == "" or self.visitor_vehicle == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                name = self.visitor_name.get();
                contact = self.visitor_contact.get();
                address = self.visitor_address.get();
                vehicle = self.visitor_vehicle.get();
                cur.execute('INSERT INTO visitors VALUES (NULL,?,?,?,?)',
                            (name, contact, address, vehicle))
                con.commit()
                messagebox.showinfo('Success', 'Gate pass created', parent=self.root)
                self.root.quit()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : str{(ex)}", parent=self.root)


root = Tk()
print('NewGatePass')
obj = NewGatePass(root)
root.mainloop()
