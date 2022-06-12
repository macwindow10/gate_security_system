import datetime
import sys
from tkinter import *
from tkinter import ttk, messagebox
import sqlite3


class ViewGatePasses:
    def __init__(self, root, userid):
        self.root = root
        self.root.geometry('1000x450+0+0')
        self.root.title('Security Management System')
        self.root.config(bg='white')
        self.root.focus_force()
        self.userid = userid

        # ------All variables---------
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        self.selected_visitor_log_id = StringVar()
        self.selected_visitor_log_approved = StringVar()
        self.selected_visitor_log_entry_time = StringVar()
        self.selected_visitor_log_valid_till = StringVar()
        self.selected_visitor_log_exit_time = StringVar()

        # ------Search Frame--------
        SearchFrame = LabelFrame(self.root, text='Search Gate Pass', font=('times new roman', 12, 'bold'), bg='white',
                                 bd=2, relief=RIDGE)
        SearchFrame.place(x=150, y=20, width=600, height=70)

        # ----Options-----
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby,
                                  values=('Select', 'Visitor Name', 'Contact', 'Vehicle'), state='readonly',
                                  justify=CENTER,
                                  font=('times now roman', 12))
        cmb_search.current(2)
        cmb_search.place(x=10, y=10, width=180)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=('times new roman', 15),
                           bg='lightyellow').place(x=200, y=10)
        btn_search = Button(SearchFrame, text='Search', command=self.search, font=('times new roman', 15), bg='#4caf50',
                            fg='white').place(x=410, y=9, width=150, height=30)

        button_enter_visitor = Button(self.root, text='Enter Visitor', command=self.enter_visitor,
                                      font=('times new roman', 15), bg='#4caf50',
                                      fg='white').place(x=200, y=130, width=150, height=30)
        button_exit_visitor = Button(self.root, text='Exit Visitor', command=self.exit_visitor,
                                     font=('times new roman', 15), bg='#4caf50',
                                     fg='white').place(x=400, y=130, width=150, height=30)

        # =============== Gate Pass Details Grid =========
        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=170, relwidth=1, height=300)
        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        # What's in columns is case sensitive cuz these headings are going to go the db
        self.gatePassTable = ttk.Treeview(emp_frame, columns=(
            'vid', 'name', 'contact', 'address', 'vehicle', 'vlid', 'approved', 'approvedbyemployeeid', 'entrytime',
            'validtill', 'exittime'),
                                          yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        # Now the scroll bar rolls bit doesnt move the headings, so we do the following
        scrollx.config(command=self.gatePassTable.xview)
        scrolly.config(command=self.gatePassTable.yview)

        self.gatePassTable.pack(fill=BOTH, expand=1)
        self.gatePassTable.heading("vid", text='Visitor ID')
        self.gatePassTable.heading("name", text='Name')
        self.gatePassTable.heading("contact", text='Contact')
        self.gatePassTable.heading("address", text='Address')
        self.gatePassTable.heading("vehicle", text='Vehicle')
        self.gatePassTable.heading("vlid", text='Gate Pass ID')
        self.gatePassTable.heading("approved", text='Approved?')
        self.gatePassTable.heading("approvedbyemployeeid", text='Approved/Rejected By')
        self.gatePassTable.heading("entrytime", text='Entry Time')
        self.gatePassTable.heading("validtill", text='Valid Till')
        self.gatePassTable.heading("exittime", text='Exit Time')
        # Remove the first empty heading
        self.gatePassTable['show'] = 'headings'

        self.gatePassTable.column("vid", width=60)
        self.gatePassTable.column("name", width=90)
        self.gatePassTable.column("contact", width=90)
        self.gatePassTable.column("address", width=90)
        self.gatePassTable.column("vehicle", width=70)
        self.gatePassTable.column("vlid", width=80)
        self.gatePassTable.column("approved", width=80)
        self.gatePassTable.column("approvedbyemployeeid", width=140)
        self.gatePassTable.column("entrytime", width=90)
        self.gatePassTable.column("validtill", width=90)
        self.gatePassTable.column("exittime", width=90)
        # Now the headings are too big, we wanna make them a bit smaller
        self.gatePassTable.pack(fill=BOTH, expand=1)
        self.gatePassTable.bind('<ButtonRelease-1>', self.get_data)
        self.show()

    # Data that's in the db should reflect
    def get_data(self, ev):
        f = self.gatePassTable.focus()
        content = (self.gatePassTable.item(f))
        row = content['values']
        print(row)
        self.selected_visitor_log_id.set(row[5])
        self.selected_visitor_log_approved.set(row[6])
        self.selected_visitor_log_entry_time.set(row[8])
        self.selected_visitor_log_valid_till.set(row[9])
        self.selected_visitor_log_exit_time.set(row[10])

    def show(self):
        con = sqlite3.connect(database=r'../ims.db')
        cur = con.cursor()
        try:
            cur.execute(
                'SELECT	v.id vid, v.name, v.contact, v.address, v.vehicle, vl.id vlid, CASE vl.approved WHEN 0 THEN \'Not Approved\' WHEN 1 THEN \'Approved\' WHEN 2 THEN \'Rejected\' END approved, e.name approvedbyemployeeid, vl.entrytime, vl.validtill, vl.exittime ' +
                'FROM visitors_log vl INNER JOIN visitors v ON vl.visitorid=v.id LEFT JOIN employee e ON vl.approvedbyemployeeid=e.eid ')
            rows = cur.fetchall()
            self.gatePassTable.delete(*self.gatePassTable.get_children())
            for row in rows:
                self.gatePassTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : str{(ex)}", parent=self.root)

    def enter_visitor(self):
        print('enter_visitor')
        print(self.selected_visitor_log_approved.get())
        print(self.selected_visitor_log_entry_time.get())
        print(self.selected_visitor_log_valid_till.get())
        print(self.selected_visitor_log_exit_time.get())

        con = sqlite3.connect(database=r'../ims.db')
        cur = con.cursor()
        try:
            if self.selected_visitor_log_id.get() == "":
                messagebox.showerror("Error", "No gate pass entry selected", parent=self.root)
                return
            if self.selected_visitor_log_approved.get() != "Approved":
                messagebox.showerror("Error", "Gate pass is not approved", parent=self.root)
                return
            if self.selected_visitor_log_entry_time.get() is None:
                messagebox.showerror("Error", "Visitor already entered on this gate pass", parent=self.root)
                return
            if self.selected_visitor_log_exit_time.get() is None:
                messagebox.showerror("Error", "Visitor already exit on this gate pass", parent=self.root)
                return

            current_date_time = datetime.datetime.now()
            cur.execute(
                'UPDATE visitors_log SET entry_time=? WHERE id=?',
                (current_date_time, self.selected_visitor_log_id))
            con.commit()
            messagebox.showinfo('Success', 'Gate pass approved', parent=self.root)
            self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : str{(ex)}", parent=self.root)

    def exit_visitor(self):
        print('exit_visitor')

    def search(self):
        con = sqlite3.connect(database=r'../ims.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get() == "Select":
                messagebox.showerror("Error", "Please select an option", parent=self.root)
            elif self.var_searchtxt.get() == '':
                messagebox.showerror("Error", "Please insert required information", parent=self.root)
            else:
                search_column_name = ''
                if self.var_searchby.get() == 'Visitor Name':
                    search_column_name = 'v.name'
                elif self.var_searchby.get() == 'Contact':
                    search_column_name = 'v.contact'
                elif self.var_searchby.get() == 'Vehicle':
                    search_column_name = 'v.vehicle'

                cur.execute(
                    'SELECT	v.id vid, v.name, v.contact, v.address, v.vehicle, vl.id vlid, CASE vl.approved WHEN 0 THEN \'Not Approved\' WHEN 1 THEN \'Approved\' WHEN 2 THEN \'Rejected\' END approved, e.name approvedbyemployeeid, vl.entrytime, vl.validtill, vl.exittime ' +
                    'FROM visitors_log vl INNER JOIN visitors v ON vl.visitorid=v.id LEFT JOIN employee e ON vl.approvedbyemployeeid=e.eid ' +
                    'WHERE ' + search_column_name + " LIKE '%" + self.var_searchtxt.get() + "%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.gatePassTable.delete(*self.gatePassTable.get_children())
                    for row in rows:
                        self.gatePassTable.insert('', END, values=row)
                else:
                    messagebox.showerror('Error', 'Record not found!', parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : str{(ex)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = ViewGatePasses(root, sys.argv[1])
    root.mainloop()
