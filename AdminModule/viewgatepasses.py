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
        self.userid = userid;

        # ------All variables---------
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        self.selected_visitor_log_id = StringVar()

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

        btn_add = Button(self.root, text='Approve Gate Pass', command=self.approve_gate_pass,
                         font=('times new roman', 15), bg='#2196f3',
                         fg='white').place(x=410, y=130, width=180, height=28)

        # =============== Gate Pass Details Grid =========
        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=170, relwidth=1, height=300)
        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        # What's in columns is case sensitive cuz these headings are going to go the db
        self.gatePassTable = ttk.Treeview(emp_frame, columns=(
            'vid', 'name', 'contact', 'address', 'vehicle', 'vlid', 'approved', 'approvedbyemployeeid', 'entrytime', 'validtill', 'exittime'),
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

    # Data thats in the db should reflect
    def get_data(self, ev):
        print('get_data')
        f = self.gatePassTable.focus()
        content = (self.gatePassTable.item(f))
        row = content['values']
        print(row)
        self.selected_visitor_log_id.set(row[5])
        print(self.selected_visitor_log_id.get())

    def show(self):
        con = sqlite3.connect(database=r'../ims.db')
        cur = con.cursor()
        try:
            cur.execute('SELECT	v.id vid, v.name, v.contact, v.address, v.vehicle, vl.id vlid, vl.approved approved, vl.approvedbyemployeeid approvedbyemployeeid, vl.entrytime, vl.validtill, vl.exittime \
                        FROM visitors_log vl INNER JOIN visitors v ON vl.visitorid=v.id \
                        WHERE vl.approvedbyemployeeid IS NULL')
            rows = cur.fetchall()
            self.gatePassTable.delete(*self.gatePassTable.get_children())
            for row in rows:
                self.gatePassTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : str{(ex)}", parent=self.root)

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
                    search_column_name = 'name'
                elif self.var_searchby.get() == 'Contact':
                    search_column_name = 'contact'
                elif self.var_searchby.get() == 'Vehicle':
                    search_column_name = 'vehicle'

                cur.execute('SELECT	v.id vid, v.name, v.contact, v.address, v.vehicle, vl.id vlid, vl.approvedbyemployeeid approved, vl.entrytime, vl.validtill, vl.exittime \
                        FROM visitors_log vl INNER JOIN visitors v ON vl.visitorid=v.id' +
                            ' WHERE ' + search_column_name + " LIKE '%" + self.var_searchtxt.get() + "%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.gatePassTable.delete(*self.gatePassTable.get_children())
                    for row in rows:
                        self.gatePassTable.insert('', END, values=row)
                else:
                    messagebox.showerror('Error', 'Record not found!', parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : str{(ex)}", parent=self.root)

    def approve_gate_pass(self):
        print('approve_gate_pass')
        con = sqlite3.connect(database=r'../ims.db')
        cur = con.cursor()
        try:
            print(self.selected_visitor_log_id.get())
            if self.selected_visitor_log_id.get() == "":
                messagebox.showerror("Error", "No gate pass entry selected", parent=self.root)
            else:
                cur.execute("SELECT * FROM visitors_log WHERE id = ? ", (self.selected_visitor_log_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid ID!", parent=self.root)
                else:
                    cur.execute(
                        'UPDATE visitors_log SET approved=?, approvedbyemployeeid=? WHERE id=?',
                        (1, self.userid, self.selected_visitor_log_id.get(),))
                    con.commit()
                    messagebox.showinfo('Success', 'Gate pass approved', parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : str{(ex)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = ViewGatePasses(root, sys.argv[1])
    root.mainloop()
