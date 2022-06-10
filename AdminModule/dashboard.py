import os
from tkinter import *

from employee import employeeClass


class IMS:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1350x700+0+0')
        self.root.title('Security Management System')
        #self.root.config(bg = 'yellow')
        
        #====title =====
#        self.icon_title = PhotoImage(file = 'images/logo1.png')
        title = Label(self.root, text = 'Security Management System',compound=LEFT, font = ('times new roman', 40, 'bold'), bg = '#011a18', fg = 'white', anchor = 'w', padx=20).place(x= 0, y = 0, relwidth = 1, height = 70)
        
        #===btn_logout=====
        btn_logout=Button(self.root, text = 'Logout', command=self.logout,font = ('times new roman', 15, 'bold'), bg = 'pink', cursor = 'hand2').place(x=800, y = 20, height = 30, width = 150)

        #====clock =====
        self.lbl_clock = Label(self.root, text = 'Welcome to Security Management System ', font = ('times new roman', 15), bg = 'black', fg = 'white')
        self.lbl_clock.place(x= 0, y = 70, relwidth = 1, height = 30)

        #===Left Menu ====
        LeftMenu = Frame(self.root, bd = 5, relief=SOLID, bg = 'white')
        LeftMenu.place(x=0, y = 102, width = 200, height = 565)
        lbl_menu = Label(LeftMenu, text = 'Menu',font = ('times new roman', 20), bg = 'green').pack(side=TOP,fill=X)
        btn_employee=Button(LeftMenu, text = 'Employee',command=self.employee,font = ('times new roman', 20, 'bold'), bg = 'yellow',bd = 3, cursor = 'hand2').pack(side=TOP,fill=X)
        
        #====Content =====
        #self.lbl_employee=Label(self.root, text = 'Total Employees\n[0]',bd = 5, relief = SOLID,bg = '#33bbf9', font = ('times new roman',20, 'bold'))
        #self.lbl_employee.place(x=300, y = 120, height = 120, width = 300)

        #self.lbl_category=Label(self.root, text = 'Total Categories\n[0]',bd = 5, relief = RIDGE,bg = '#33bbf9', font = ('times new roman',20, 'bold'))
        #self.lbl_category.place(x=650, y = 120, height = 120, width = 300)

        #self.lbl_item=Label(self.root, text = 'Total Items\n[0]',bd = 5, relief = RIDGE,bg = '#33bbf9', font = ('times new roman',20, 'bold'))
        #self.lbl_item.place(x=300, y = 300, height = 120, width = 300)

        #self.lbl_sales=Label(self.root, text = 'Total Sales\n[0]',bd = 5, relief = RIDGE,bg = '#33bbf9', font = ('times new roman',20, 'bold'))
        #self.lbl_sales.place(x=650, y = 300, height = 120, width = 300)

    
        #====footer =====
        lbl_footer = Label(self.root, text ='B M S', font = ('times new roman', 12), bg = '#4d636d', fg = 'white').pack(side = BOTTOM, fill = X)

        #self.update_content()
#==========================================================================
    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = employeeClass(self.new_win)
        

    
    
        #try:
   #         cur.execute('select * from product')
    #        product = cur.fetchall()
     #       self.lbl_item.config(text = f'Total Items \n [{str(len(product))}]')




      #      cur.execute('select * from category')
       #     category = cur.fetchall()
        #    self.lbl_category.config(text = f'Categories \n [{str(len(category))}]')



         #   cur.execute('select * from employee')
          #  employee = cur.fetchall()
           # self.lbl_employee.config(text = f'Total Employees \n [{str(len(employee))}]')


            #time_ = time.strftime("%I:::%M::::%S") 
            #date_ = time.strftime("%d-%m-%Y")
            #self.lbl_clock.config( text = f'Welcome to Bakery Management System \t\t Date: {str(date_)} \t\t Time: {str(time_)}' )        
            #self.lbl_clock.after(5000,self.update_content)




#        except Exception as ex:
 #           messagebox.showerror("Error",f"Error due to : str{(ex)}",parent = self.root)

    def logout(self):
        self.root.destroy()
        os.system('python login.py')


if __name__ =="__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()



