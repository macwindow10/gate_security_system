import os
import sys
from tkinter import *


class DashboardGuard:
    def __init__(self, root, role, userid, username):
        self.root = root
        self.root.geometry('1350x700+0+0')
        self.root.title('Security Management System')
        self.role = role
        self.userid = userid
        self.username = username

        title = Label(self.root, text='Security Management System', compound=LEFT, font=('times new roman', 40, 'bold'),
                      bg='#011a18', fg='white', anchor='w', padx=20).place(x=0, y=0, relwidth=1, height=70)

        # ===btn_logout=====
        btn_logout = Button(self.root, text='Logout', command=self.logout, font=('times new roman', 15, 'bold'),
                            bg='pink', cursor='hand2').place(x=800, y=20, height=30, width=150)

        # ====clock =====
        self.lbl_clock = Label(self.root, text='Welcome to Security Management System - {} ({})'.format(self.username, self.role), font=('times new roman', 15),
                               bg='black', fg='white')
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

        # ===Left Menu ====
        LeftMenu = Frame(self.root, bd=5, relief=SOLID, bg='white')
        LeftMenu.place(x=0, y=102, width=200, height=565)
        lbl_menu = Label(LeftMenu, text='Menu', font=('times new roman', 16, 'bold'), bg='green').pack(side=TOP, fill=X)
        btn_newgatepass = Button(LeftMenu, text='New Gate Pass', command=self.button_newgatepass,
                                 font=('times new roman', 16, 'bold'),
                                 bg='yellow', bd=3, cursor='hand2').pack(side=TOP, fill=X)
        btn_viewgatepasses = Button(LeftMenu, text='View Gate Passes', command=self.button_viewgatepasses,
                                 font=('times new roman', 16, 'bold'),
                                 bg='yellow', bd=3, cursor='hand2').pack(side=TOP, fill=X)

    def button_newgatepass(self):
        print('button_newgatepass')
        # self.root.destroy()
        os.system('python newgatepass.py')

    def button_viewgatepasses(self):
        print('button_viewgatepasses')
        # self.root.destroy()
        os.system('python viewgatepasses.py {}'.format(self.userid))

    def logout(self):
        self.root.destroy()
        os.system('python login.py')


if __name__ == "__main__":
    root = Tk()
    print('DashboardGuard')
    obj = DashboardGuard(root, sys.argv[1], sys.argv[2], sys.argv[3])
    root.mainloop()
