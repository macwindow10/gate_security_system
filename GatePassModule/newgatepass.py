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
        self.visitor_co_visitors = StringVar()
        self.visitor_belongings = StringVar()
        self.host_name = StringVar()
        self.host_contact = StringVar()

        new_gate_pass_frame = Frame(self.root, bd=4, relief=RIDGE, bg='white')
        new_gate_pass_frame.place(x=360, y=50, width=400, height=550)

        font = tkinter.font.Font(name='times new roman', size=16)
        Label(new_gate_pass_frame, text='New Gate Pass', font=font, bg='#262626', fg='white').pack(
            side=TOP, fill=X)

        Label(new_gate_pass_frame, text='Visitor Name: ', font=font,
              bg='lightgrey').place(x=2, y=100)
        Entry(new_gate_pass_frame, textvariable=self.visitor_name,
              font=font).place(x=200, y=100, width=170, height=32)

        Label(new_gate_pass_frame, text='Visitor Contact: ', font=font, bg='lightgrey').place(x=2, y=150)
        Entry(new_gate_pass_frame, textvariable=self.visitor_contact,
              font=font).place(x=200, y=150, width=170, height=32)

        Label(new_gate_pass_frame, text='Visitor Address: ', font=font, bg='lightgrey').place(x=2, y=200)
        Entry(new_gate_pass_frame, textvariable=self.visitor_address,
              font=font).place(x=200, y=200, width=170, height=32)

        Label(new_gate_pass_frame, text='Visitor Vehicle: ', font=font, bg='lightgrey').place(x=2,
                                                                                              y=250)
        Entry(new_gate_pass_frame, textvariable=self.visitor_vehicle,
              font=font).place(x=200, y=250, width=170, height=32)

        Label(new_gate_pass_frame, text='Co-Visitor Name(s): ', font=font, bg='lightgrey').place(x=2,
                                                                                                 y=300)
        Entry(new_gate_pass_frame, textvariable=self.visitor_co_visitors,
              font=font).place(x=200, y=300, width=170, height=32)

        Label(new_gate_pass_frame, text='Visitor Belongings: ', font=font,
              bg='lightgrey').place(x=2, y=350)
        Entry(new_gate_pass_frame, textvariable=self.visitor_belongings,
              font=font).place(x=200, y=350, width=170, height=32)

        Label(new_gate_pass_frame, text='Host Name: ', font=font,
              bg='lightgrey').place(x=2, y=400)
        Entry(new_gate_pass_frame, textvariable=self.host_name,
              font=font).place(x=200, y=400, width=170, height=32)

        Label(new_gate_pass_frame, text='Host Contact: ', font=font,
              bg='lightgrey').place(x=2, y=450)
        Entry(new_gate_pass_frame, textvariable=self.host_contact,
              font=font).place(x=200, y=450, width=170, height=32)

        Button(new_gate_pass_frame, text='Create', command=self.create_gate_pass,
               font=font,
               bg='red', fg='white').place(x=200, y=500, width=100, height=25)

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
                co_visitors = self.visitor_co_visitors.get();
                belongings = self.visitor_belongings.get();
                host_name = self.host_name.get();
                host_contact = self.host_contact.get();
                cur.execute('INSERT INTO visitors VALUES (NULL,?,?,?,?,?,?,?,?)',
                            (name, contact, address, vehicle, co_visitors, belongings, host_name, host_contact))

                print('row id : ' + str(cur.lastrowid))
                cur.execute('INSERT INTO visitors_log(visitorid) VALUES(?)',
                            (cur.lastrowid,))
                con.commit()

                messagebox.showinfo('Success', 'Gate pass created', parent=self.root)
                self.root.quit()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : str{(ex)}", parent=self.root)


root = Tk()
print('NewGatePass')
obj = NewGatePass(root)
root.mainloop()
