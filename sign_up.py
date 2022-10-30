from tkinter import*
# from PIL import Image,ImageTk
from tkinter import ttk
import time
import sqlite3
from tkinter import messagebox
import os

# dk=Tk()
class sign_up:
    def __init__(self,dk):
        self.dk=dk
        self.dk.geometry("1350x700+0+0")
        self.dk.title("Inventory Management System  | by dk")
        self.dk.config(bg="cyan")
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

# =================== images ==================
        self.menulogo=PhotoImage(file="images/menu_imm.png")
        self.update_date_time()
        #===========================
        # all variable

        self.var_emp_id=StringVar()
        self.var_emp_gender=StringVar()
        self.var_emp_contact=StringVar()
        self.var_emp_name=StringVar()
        self.var_emp_email=StringVar()
        self.var_emp_dob=StringVar()
        self.var_emp_doj=StringVar()
        self.var_emp_password=StringVar()
        self.var_emp_userType=StringVar()
        
         # title ====
        title=Label(self.dk,text="Employee Details",font=("goudy old style",25,"bold"),bg="cyan4",fg="white").place(x=180,y=150,width=1000,height=40)

        # content ===
        # row1=======
        lbl_empid=Label(self.dk,text="Employee ID",font=("goudy old style",15,"bold"),bg="cyan").place(x=180,y=250)
        lbl_gender=Label(self.dk,text="Gender",font=("goudy old style",15,"bold"),bg="cyan").place(x=540,y=250)
        lbl_contact=Label(self.dk,text="Contact",font=("goudy old style",15,"bold"),bg="cyan").place(x=870,y=250)
        
        
        text_empid=Entry(self.dk,textvariable=self.var_emp_id,font=("goudy old style",15,"bold"),bg="light yellow").place(x=330,y=250,width=180)
        text_gender=Entry(self.dk,textvariable=self.var_emp_gender,font=("goudy old style",15,"bold"),bg="light yellow").place(x=650,y=250,width=180)
        cmb_gender=ttk.Combobox(self.dk,textvariable=self.var_emp_gender,values=("Select","Male","Female","Other"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_gender.place(x=650,y=250,width=180)
        cmb_gender.current(0)
        text_contact=Entry(self.dk,textvariable=self.var_emp_contact,font=("goudy old style",15,"bold"),bg="light yellow").place(x=950,y=250,width=180)

# ============================ row2 ===========================

        lbl_name=Label(self.dk,text="Name",font=("goudy old style",15,"bold"),bg="cyan").place(x=180,y=350)
        lbl_dob=Label(self.dk,text="D.O.B",font=("goudy old style",15,"bold"),bg="cyan").place(x=540,y=350)
        lbl_doj=Label(self.dk,text="D.O.J",font=("goudy old style",15,"bold"),bg="cyan").place(x=870,y=350)
        
        text_name=Entry(self.dk,textvariable=self.var_emp_name,font=("goudy old style",15,"bold"),bg="light yellow").place(x=330,y=350,width=180)
        text_dob=Entry(self.dk,textvariable=self.var_emp_dob,font=("goudy old style",15,"bold"),bg="light yellow").place(x=650,y=350,width=180)
        text_doj=Entry(self.dk,textvariable=self.var_emp_doj,font=("goudy old style",15,"bold"),bg="light yellow").place(x=950,y=350,width=180)

        # row3==============

        lbl_email=Label(self.dk,text="Email",font=("goudy old style",15,"bold"),bg="cyan").place(x=180,y=450)
        lbl_password=Label(self.dk,text="Password",font=("goudy old style",15,"bold"),bg="cyan").place(x=540,y=450)
        lbl_usertype=Label(self.dk,text="User Type",font=("goudy old style",15,"bold"),bg="cyan").place(x=870,y=450)
        
        text_email=Entry(self.dk,textvariable=self.var_emp_email,font=("goudy old style",15,"bold"),bg="light yellow").place(x=330,y=450,width=180)
        text_password=Entry(self.dk,textvariable=self.var_emp_password,font=("goudy old style",15,"bold"),bg="light yellow").place(x=650,y=450,width=180)
        text_usertype=Entry(self.dk,textvariable=self.var_emp_userType,font=("goudy old style",15,"bold"),bg="light yellow").place(x=980,y=450,width=180)
        cmb_usertype=ttk.Combobox(self.dk,textvariable=self.var_emp_userType,values=("Employee"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_usertype.place(x=980,y=450,width=180)
        cmb_usertype.current(0)

        lbl_address=Label(self.dk,text="Address",font=("goudy old style",15,"bold"),bg="cyan").place(x=180,y=550)
        
        self.text_address=Text(self.dk,font=("goudy old style",15,"bold"),bg="light yellow")
        self.text_address.place(x=320,y=540,width=300,height=60)
        

         # button ==================
        btm_save=Button(self.dk,text="Save",command=self.add,font=("goudy old style",15,"bold"),bg="deep pink",fg="white",cursor="hand2").place(x=660,y=560,width=110,height=30)
        
        btm_clear=Button(self.dk,text="Clear",command=self.clear,font=("goudy old style",15,"bold"),bg="Dark Orange1",fg="white",cursor="hand2").place(x=800,y=560,width=110,height=30)



# ============================all function =================
    def add(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("error","employee ID must be required",parent=self.dk)
            else:
                cur.execute("select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("error","this employee id already assigned ,try another",parent=self.dk)
                else:
                    cur.execute("Insert into employee (eid,name,email,gender,contact,dob,doj,password,userType,address) values(?,?,?,?,?,?,?,?,?,?)",(
                    self.var_emp_id.get(),
                    self.var_emp_name.get(),
                    self.var_emp_email.get(),
                    self.var_emp_gender.get(),
                    self.var_emp_contact.get(),
                    self.var_emp_dob.get(),
                    self.var_emp_doj.get(),
                    self.var_emp_password.get(),
                    self.var_emp_userType.get(),
                    self.text_address.get('1.0',END)
                    ))
                    con.commit()
                    messagebox.showinfo("success","employee added successfully",parent=self.dk)
        except Exception as ex:
            messagebox.showerror("error",f"error due to : {str(ex)}",parent=self.dk)


    def clear(self):
        self.var_emp_id.set("")
        self.var_emp_name.set("")
        self.var_emp_email.set("")
        self.var_emp_gender.set("Select")
        self.var_emp_contact.set("")
        self.var_emp_dob.set("")
        self.var_emp_doj.set("")
        self.var_emp_password.set("")
        self.var_emp_userType.set("Select")
        self.text_address.delete('1.0',END)
        # self.text_address.insert(END,row[9])
        
        













    def update_date_time(self):
        time_in=time.strftime("%I-%M-%S")
        date_in=time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"Welcome to Inventory Management System\t\t Date:- {str(date_in)}\t\t Time:- {str(time_in)}")
        self.lbl_clock.after(200,self.update_date_time)

    def logout(self):
        self.dk.destroy()
        os.system("python login.py")











if __name__=="__main__":
    dk=Tk()
    obj=sign_up(dk)
    dk.mainloop()