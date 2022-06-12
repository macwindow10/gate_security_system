from tkinter import *
from tkinter import ttk, messagebox
import sqlite3


class employeeClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('880x450+0+0')
        self.root.title('Security Management System')
        self.root.config(bg='white')
        self.root.focus_force()

        # ------All variables---------
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_emp_id = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_utype = StringVar()
        self.var_salary = StringVar()

        # ------Search Frame--------
        SearchFrame = LabelFrame(self.root, text='Search Employee', font=('times new roman', 12, 'bold'), bg='white',
                                 bd=2, relief=RIDGE)
        SearchFrame.place(x=250, y=20, width=600, height=70)

        # ----Options-----
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby,
                                  values=('Select', 'Email', 'Name', 'Contact'), state='readonly', justify=CENTER,
                                  font=('times now roman', 12))
        cmb_search.current(2)
        cmb_search.place(x=10, y=10, width=180)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=('times new roman', 15),
                           bg='lightyellow').place(x=200, y=10)
        btn_search = Button(SearchFrame, text='Search', command=self.search, font=('times new roman', 15), bg='#4caf50',
                            fg='white').place(x=410, y=9, width=150, height=30)

        # ----Title-----
        title = Label(self.root, text='Employee Details', font=('times new roman', 15), bg='#0f4d7d', fg='white').place(
            x=50, y=100, width=800)

        # ----Content-----
        # ----Row 1 ------
        lbl_empid = Label(self.root, text='Emp ID', font=('times new roman', 15), bg='white').place(x=50, y=150)
        lbl_gender = Label(self.root, text='Gender', font=('times new roman', 15), bg='white').place(x=350, y=150)
        lbl_contact = Label(self.root, text='Contact', font=('times new roman', 15), bg='white').place(x=750, y=150)

        txt_empid = Entry(self.root, textvariable=self.var_emp_id, font=('times new roman', 15),
                          bg='lightyellow').place(x=150, y=150, width=180)
        # txt_gender = Entry(self.root, textvariable= self.var_gender, font = ('times new roman',15), bg = 'white').place( x = 500 , y = 150, width=180)
        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=('Select', 'Male', 'Female', 'Other'),
                                  state='readonly', justify=CENTER, font=('times now roman', 12))
        cmb_gender.current(0)
        cmb_gender.place(x=500, y=150, width=180)

        txt_contact = Entry(self.root, textvariable=self.var_contact, font=('times new roman', 15),
                            bg='lightyellow').place(x=850, y=150, width=180)

        # =========Row 2========
        lbl_name = Label(self.root, text='Name', font=('times new roman', 15), bg='white').place(x=50, y=190)
        lbl_dob = Label(self.root, text='D.O.B', font=('times new roman', 15), bg='white').place(x=350, y=190)
        lbl_doj = Label(self.root, text='D.O.J', font=('times new roman', 15), bg='white').place(x=750, y=190)

        txt_name = Entry(self.root, textvariable=self.var_name, font=('times new roman', 15), bg='lightyellow').place(
            x=150, y=190, width=180)
        txt_dob = Entry(self.root, textvariable=self.var_dob, font=('times new roman', 15), bg='lightyellow').place(
            x=500, y=190, width=180)
        txt_doj = Entry(self.root, textvariable=self.var_doj, font=('times new roman', 15), bg='lightyellow').place(
            x=850, y=190, width=180)

        # =========Row 3========
        lbl_email = Label(self.root, text='Email', font=('times new roman', 15), bg='white').place(x=50, y=230)
        lbl_pass = Label(self.root, text='Password', font=('times new roman', 15), bg='white').place(x=350, y=230)
        lbl_utype = Label(self.root, text='User Type', font=('times new roman', 15), bg='white').place(x=750, y=230)

        txt_email = Entry(self.root, textvariable=self.var_email, font=('times new roman', 15), bg='lightyellow').place(
            x=150, y=230, width=180)
        txt_pass = Entry(self.root, textvariable=self.var_pass, font=('times new roman', 15), bg='lightyellow').place(
            x=500, y=230, width=180)
        # txt_utype = Entry(self.root, textvariable= self.var_utype, font = ('times new roman',15), bg = 'lightyellow').place( x = 850 , y = 230, width=180)
        cmb_utype = ttk.Combobox(self.root, textvariable=self.var_utype, values=('Admin', 'Manager', 'Guard'),
                                 state='readonly', justify=CENTER, font=('times now roman', 12))
        cmb_utype.current(0)
        cmb_utype.place(x=850, y=230, width=180)

        # =========Row 4========
        lbl_address = Label(self.root, text='Address', font=('times new roman', 15), bg='white').place(x=50, y=270)
        lbl_salary = Label(self.root, text='Salary', font=('times new roman', 15), bg='white').place(x=500, y=270)

        self.txt_address = Text(self.root, font=('times new roman', 15), bg='lightyellow')
        self.txt_address.place(x=150, y=270, width=300, height=60)
        txt_salary = Entry(self.root, textvariable=self.var_salary, font=('times new roman', 15),
                           bg='lightyellow').place(x=600, y=270, width=180)

        # -----Button -----
        # command self.**** links the button to the database querry.
        btn_add = Button(self.root, text='Save', command=self.add, font=('times new roman', 15), bg='#2196f3',
                         fg='white').place(x=500, y=305, width=110, height=28)
        btn_update = Button(self.root, text='Update', command=self.update, font=('times new roman', 15), bg='#2196f3',
                            fg='white').place(x=620, y=305, width=110, height=28)
        btn_delete = Button(self.root, text='Delete', command=self.delete, font=('times new roman', 15), bg='#2196f3',
                            fg='white').place(x=740, y=305, width=110, height=28)
        btn_clear = Button(self.root, text='Clear', command=self.clear, font=('times new roman', 15), bg='#2196f3',
                           fg='white').place(x=860, y=305, width=110, height=28)

        # =============== Employee Details Tree View=========
        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        # emp_frame.place(x=0,y=350,relwidth = 1,height = 150)
        emp_frame.place(x=0, y=350, relwidth=1, height=150)
        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        # Whats in columns is case senstive cuz these headings are going to go the db

        self.EmployeeTable = ttk.Treeview(emp_frame, columns=(
        'eid', 'name', 'email', 'gender', 'contact', 'dob', 'doj', 'pass', 'utype', 'address', 'salary'),
                                          yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        # Now the scroll bar rolls bit doesnt move the headings, so we do the following
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)

        self.EmployeeTable.pack(fill=BOTH, expand=1)
        self.EmployeeTable.heading("eid", text='EMPPP')
        self.EmployeeTable.heading("name", text='Name')
        self.EmployeeTable.heading("email", text='Email')
        self.EmployeeTable.heading("gender", text='Gender')
        self.EmployeeTable.heading("contact", text='Contact')
        #       self.EmployeeTable.heading("dob", text='D.O.B')
        self.EmployeeTable.heading("dob", text='D.O.B')
        self.EmployeeTable.heading("doj", text='D.O.J')
        self.EmployeeTable.heading("pass", text='Password')
        self.EmployeeTable.heading("utype", text='User Type')
        self.EmployeeTable.heading("address", text='Address')
        self.EmployeeTable.heading("salary", text='Salary')
        # Remove the first empty heading
        self.EmployeeTable['show'] = 'headings'

        self.EmployeeTable.column("eid", width=30)
        self.EmployeeTable.column("name", width=90)
        self.EmployeeTable.column("email", width=90)
        self.EmployeeTable.column("gender", width=90)
        self.EmployeeTable.column("contact", width=90)
        #       self.EmployeeTable.heading("dob", text='D.O.B')
        self.EmployeeTable.column("dob", width=90)
        self.EmployeeTable.column("doj", width=90)
        self.EmployeeTable.column("pass", width=90)
        self.EmployeeTable.column("utype", width=90)
        self.EmployeeTable.column("address", width=90)
        self.EmployeeTable.column("salary", width=90)
        # Now the headings are too big, we wanna make them a bit smaller

        self.EmployeeTable.pack(fill=BOTH, expand=1)
        self.EmployeeTable.bind('<ButtonRelease-1>', self.get_data)
        self.show()

    # Now we have created a database using create_db.py and created an
    # employee table as well. Now we are going to work on the
    # Functionality of the buttons to insert and modify data in the table etc.

    # Add button
    def add(self):
        con = sqlite3.connect(database=r'../ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID is required", parent=self.root)
            else:
                cur.execute("Select * from employee where eid = ? ", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Employee ID already in use!", parent=self.root)
                else:
                    cur.execute(
                        'Insert into employee ( eid , name , email ,  gender , contact , dob , doj , pass , utype , address , salary ) values(?,?,?,?,?,?,?,?,?,?,?)',
                        (
                            self.var_emp_id.get(),
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_contact.get(),
                            self.var_dob.get(),
                            self.var_doj.get(),
                            self.var_pass.get(),
                            self.var_utype.get(),
                            self.txt_address.get('1.0', END),
                            self.var_salary.get(),

                        ))
                    con.commit()
                    messagebox.showinfo('Success', 'Employee added successfully', parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : str{(ex)}", parent=self.root)

    # Now display the data...update and other fucntions have yet to be added
    def show(self):
        con = sqlite3.connect(database=r'../ims.db')
        cur = con.cursor()
        try:
            cur.execute('select  * from employee')
            # above Doesnt need to be commited
            rows = cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : str{(ex)}", parent=self.root)

    # Data thats in the db should reflect
    def get_data(self, ev):
        f = self.EmployeeTable.focus()
        content = (self.EmployeeTable.item(f))
        row = content['values']
        print(row)
        self.var_emp_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_contact.set(row[4]),
        self.var_dob.set(row[5]),
        self.var_doj.set(row[6]),
        self.var_pass.set(row[7]),
        self.var_utype.set(row[8]),
        self.txt_address.delete('1.0', END),
        self.txt_address.insert(END, row[9]),
        self.var_salary.set(row[10]),

    # Update querry associated with update button
    def update(self):
        con = sqlite3.connect(database=r'../ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID is required", parent=self.root)
            else:
                cur.execute("Select * from employee where eid = ? ", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid ID!", parent=self.root)
                else:
                    cur.execute(
                        'Update employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=? where eid=?',
                        (
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_contact.get(),
                            self.var_dob.get(),
                            self.var_doj.get(),
                            self.var_pass.get(),
                            self.var_utype.get(),
                            self.txt_address.get('1.0', END),
                            self.var_salary.get(),
                            self.var_emp_id.get(),

                        ))
                    con.commit()
                    messagebox.showinfo('Success', 'Employee updated successfully', parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : str{(ex)}", parent=self.root)

    # Now delete querry
    def delete(self):
        con = sqlite3.connect(database=r'../ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID is required", parent=self.root)
            else:
                cur.execute("Select * from employee where eid = ? ", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid ID!", parent=self.root)
                else:
                    op = messagebox.askyesno('Confirm', 'Delete the selected record?', parent=self.root)
                    if op == True:
                        cur.execute('delete from employee where eid = ?', (self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo('Delete', 'Employee deleted successfully', parent=self.root)
                        # self.show()
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : str{(ex)}", parent=self.root)

    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_pass.set("")
        self.var_utype.set("Admin")
        self.txt_address.delete('1.0', END)
        self.var_salary.set("")
        self.var_searchtxt.set("")
        # self.var_searchbt.set("Select")
        self.show()

    # Now search querry
    def search(self):
        con = sqlite3.connect(database=r'../ims.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get() == "Select":
                messagebox.showerror("Error", "Please select an option", parent=self.root)
            elif self.var_searchtxt.get() == '':
                messagebox.showerror("Error", "Please insert required information", parent=self.root)
            else:

                cur.execute(
                    "select * from employee where " + self.var_searchby.get() + " LIKE '%" + self.var_searchtxt.get() + "%'")
                # above Doesnt need to be commited
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('', END, values=row)
                else:
                    messagebox.showerror('Error', 'Record not found!', parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : str{(ex)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = employeeClass(root)
    root.mainloop()
