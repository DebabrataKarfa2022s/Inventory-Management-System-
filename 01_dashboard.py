from tkinter import*
# from PIL import Image,ImageTk
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product  import  productClass
from sales    import    salesClass
import time
import sqlite3
from tkinter import messagebox
import os

# dk=Tk()
class IMS:
    def __init__(self,dk):
        self.dk=dk
        self.dk.geometry("1350x700+0+0")
        self.dk.title("Inventory Management System  | by dk")
        self.dk.config(bg="white")
# ================image==========================
        self.icon_title=PhotoImage(file="images/logo1.png")
        #===title===
        title=Label(self.dk,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="blue",fg="white",anchor="w",padx=20)
        title.place(x=0,y=0,relwidth=1,height=70)

        #====logout_botton===
        btn_logout=Button(self.dk,text="Logout",command=self.logout,font=("times new roman",20,"bold"),bg="yellow",cursor="hand2")
        btn_logout.place(x=1150,y=10,height=50,width=150)

        # clock
        self.lbl_clock=Label(self.dk,text="Welcome to Inventory Management System\t\t Date:-DD:MM:YYYY\t\t Time:- HH:MM:SS",font=("times new roman",15,),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        # ====left menu====
        # self.menulogo=Image.open("images/menu_im.png")
        # sefl.menulogo=self.menulogo.resize((200,200),Image.ANTIALIAS)

        self.menulogo=PhotoImage(file="images/menu_imm.png")

        leftMenu=Frame(self.dk,bd=2,relief=RIDGE,bg="white")
        leftMenu.place(x=0,y=102,width=200,height=565)

        lbl_menulogo=Label(leftMenu,image=self.menulogo)
        lbl_menulogo.pack(side=TOP,fill="x")

        # =====left_menu_buttom=====
        self.icon_side=PhotoImage(file="images/side.png")
        lbl_menu=Label(leftMenu,text="Menu",font=("tiems new roman",20),bg="green").pack(side=TOP,fill=X)
        btn_employee=Button(leftMenu,text="Employee",command=self.employee_win,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),fg="#D0D020",bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier=Button(leftMenu,text="Supplier",command=self.supplier_win,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),fg="#8B8B36",bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_Category=Button(leftMenu,text="Category",command=self.category_win,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),fg="#0000F5",bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_Product=Button(leftMenu,text="Product",command=self.product_win,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),fg="cyan2",bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_Sales=Button(leftMenu,text="Sales",command=self.sales_win,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),fg="purple",bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_Exit=Button(leftMenu,text="Exit",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),fg="maroon1",bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)


        #====content===

        self.lbl_employee=Label(self.dk,text="Toal Empolyee\n [0]",bd=6,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)

        self.lbl_Supplier=Label(self.dk,text="Toal Supplier\n [0]",bd=6,relief=RIDGE,bg="dark violet",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_Supplier.place(x=650,y=120,height=150,width=300)

        self.lbl_Category=Label(self.dk,text="Toal Category\n [0]",bd=6,relief=RIDGE,bg="#009688",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_Category.place(x=1000,y=120,height=150,width=300)

        self.lbl_Product=Label(self.dk,text="Toal Product\n [0]",bd=6,relief=RIDGE,bg="OliveDrab2",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_Product.place(x=300,y=300,height=150,width=300)

        self.lbl_Selse=Label(self.dk,text="Toal Selse\n [0]",bd=6,relief=RIDGE,bg="deep pink",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_Selse.place(x=650,y=300,height=150,width=300)

        # footer
        lbl_footer=Label(self.dk,text="Inventory Management System | dk | any problem contact me 8436832600 ",font=("times new roman",17,),bg="spring green",fg="white")
        lbl_footer.pack(side=BOTTOM,fill=X)

        # self.update_date_time()
        self.update_content()
#***************************************************************************************************************************

    def employee_win(self):
        self.new_win=Toplevel(self.dk)
        self.new_obj=employeeClass(self.new_win)

    def supplier_win(self):
        self.new_win=Toplevel(self.dk)
        self.new_obj=supplierClass(self.new_win)

    def category_win(self):
        self.new_win=Toplevel(self.dk)
        self.new_obj=categoryClass(self.new_win)

    def product_win(self):
        self.new_win=Toplevel(self.dk)
        self.new_obj=productClass(self.new_win)

    def sales_win(self):
        self.new_win=Toplevel(self.dk)
        self.new_obj=salesClass(self.new_win)

    def update_content(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            product=cur.fetchall()
            self.lbl_Product.config(text=f"Total Product\n [{str(len(product))}]")

            cur.execute("select * from supplier")
            supplier=cur.fetchall()
            self.lbl_Supplier.config(text=f"Total Supplier\n [{str(len(supplier))}]")

            cur.execute("select * from category")
            cetegory=cur.fetchall()
            self.lbl_Category.config(text=f"Total Category\n [{str(len(cetegory))}]")

            cur.execute("select * from employee")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f"Total Employee\n [{str(len(employee))}]")

            bill=len(os.listdir('bill'))
            self.lbl_Selse.config(text=f"Total Sales\n [{str(bill)}]")

            time_in=time.strftime("%I-%M-%S")
            date_in=time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f"Welcome to Inventory Management System\t\t Date:- {str(date_in)}\t\t Time:- {str(time_in)}")
            self.lbl_clock.after(200,self.update_content)


        except Exception as ex:
            messagebox.showerror("error",f"error due to : {str(ex)}",parent=self.dk)


    def logout(self):
        self.dk.destroy()
        os.system("python login.py")



    # def update_date_time(self):
    #     time_in=time.strftime("%I-%M-%S")
    #     date_in=time.strftime("%d-%m-%Y")
    #     self.lbl_clock.config(text=f"Welcome to Inventory Management System\t\t Date:- {str(date_in)}\t\t Time:- {str(time_in)}")
    #     self.lbl_clock.after(200,self.update_date_time)


    
if __name__=="__main__":
    dk=Tk()
    obj=IMS(dk)
    dk.mainloop()


