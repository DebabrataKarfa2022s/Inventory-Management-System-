from tkinter import*
# from PIL import Image,ImageTk
from tkinter import ttk ,messagebox
import sqlite3
# dk=Tk()
class employeeClass:
    def __init__(self,dk):
        self.dk=dk
        self.dk.geometry("1100x500+220+130")
        self.dk.title("Inventory Management System  | by dk")
        self.dk.config(bg="white")
        self.dk.focus_force()
        #===========================
        # all variable
        self.var_sarchby=StringVar()
        self.var_searchtext=StringVar()


        self.var_emp_id=StringVar()
        self.var_emp_gender=StringVar()
        self.var_emp_contact=StringVar()
        self.var_emp_name=StringVar()
        self.var_emp_email=StringVar()
        self.var_emp_dob=StringVar()
        self.var_emp_doj=StringVar()
        self.var_emp_password=StringVar()
        self.var_emp_userType=StringVar()
        self.var_emp_salary=StringVar()


        # sarchframe===
        sarchframe=LabelFrame(self.dk,text="Serch Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        sarchframe.place(x=250,y=20,width=600,height=70)
        # option====
        cmb_sarch=ttk.Combobox(sarchframe,textvariable=self.var_sarchby,values=("Select","Email","Name","Contact"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_sarch.place(x=10,y=10,width=180)
        cmb_sarch.current(0)
        # search button 
        text_sarch=Entry(sarchframe,textvariable=self.var_searchtext,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btm_sarch=Button(sarchframe,text="Search",command=self.search,font=("goudy old style",15,"bold"),bg="red",fg="white",cursor="hand2").place(x=420,y=9,width=150,height=30)

        # title ====
        title=Label(self.dk,text="Employee Details",font=("goudy old style",15,"bold"),bg="cyan4",fg="white").place(x=50,y=100,width=1000)

        # content ===
        # row1=======
        lbl_empid=Label(self.dk,text="Employee ID",font=("goudy old style",15,"bold"),bg="white").place(x=50,y=150)
        lbl_gender=Label(self.dk,text="Gender",font=("goudy old style",15,"bold"),bg="white").place(x=370,y=150)
        lbl_contact=Label(self.dk,text="Contact",font=("goudy old style",15,"bold"),bg="white").place(x=750,y=150)
        
        
        text_empid=Entry(self.dk,textvariable=self.var_emp_id,font=("goudy old style",15,"bold"),bg="light yellow").place(x=170,y=150,width=180)
        text_gender=Entry(self.dk,textvariable=self.var_emp_gender,font=("goudy old style",15,"bold"),bg="light yellow").place(x=500,y=150,width=180)
        cmb_gender=ttk.Combobox(self.dk,textvariable=self.var_emp_gender,values=("Select","Male","Female","Other"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_gender.place(x=500,y=150,width=180)
        cmb_gender.current(0)
        text_contact=Entry(self.dk,textvariable=self.var_emp_contact,font=("goudy old style",15,"bold"),bg="light yellow").place(x=850,y=150,width=180)

        # row2======
        
        lbl_name=Label(self.dk,text="Name",font=("goudy old style",15,"bold"),bg="white").place(x=50,y=190)
        lbl_dob=Label(self.dk,text="D.O.B",font=("goudy old style",15,"bold"),bg="white").place(x=370,y=190)
        lbl_doj=Label(self.dk,text="D.O.J",font=("goudy old style",15,"bold"),bg="white").place(x=750,y=190)
        
        text_name=Entry(self.dk,textvariable=self.var_emp_name,font=("goudy old style",15,"bold"),bg="light yellow").place(x=170,y=190,width=180)
        text_dob=Entry(self.dk,textvariable=self.var_emp_dob,font=("goudy old style",15,"bold"),bg="light yellow").place(x=500,y=190,width=180)
        text_doj=Entry(self.dk,textvariable=self.var_emp_doj,font=("goudy old style",15,"bold"),bg="light yellow").place(x=850,y=190,width=180)

        # row3==============

        lbl_email=Label(self.dk,text="Email",font=("goudy old style",15,"bold"),bg="white").place(x=50,y=230)
        lbl_password=Label(self.dk,text="Password",font=("goudy old style",15,"bold"),bg="white").place(x=370,y=230)
        lbl_usertype=Label(self.dk,text="User Type",font=("goudy old style",15,"bold"),bg="white").place(x=750,y=230)
        
        text_email=Entry(self.dk,textvariable=self.var_emp_email,font=("goudy old style",15,"bold"),bg="light yellow").place(x=170,y=230,width=180)
        text_password=Entry(self.dk,textvariable=self.var_emp_password,font=("goudy old style",15,"bold"),bg="light yellow").place(x=500,y=230,width=180)
        text_usertype=Entry(self.dk,textvariable=self.var_emp_userType,font=("goudy old style",15,"bold"),bg="light yellow").place(x=850,y=230,width=180)
        cmb_usertype=ttk.Combobox(self.dk,textvariable=self.var_emp_userType,values=("Admin","Employee"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_usertype.place(x=850,y=230,width=180)
        cmb_usertype.current(0)

        # row4=====
        lbl_address=Label(self.dk,text="Address",font=("goudy old style",15,"bold"),bg="white").place(x=50,y=270)
        lbl_salary=Label(self.dk,text="Salary",font=("goudy old style",15,"bold"),bg="white").place(x=500,y=270)
            
        self.text_address=Text(self.dk,font=("goudy old style",15,"bold"),bg="light yellow")
        self.text_address.place(x=150,y=270,width=300,height=60)
        text_salary=Entry(self.dk,textvariable=self.var_emp_salary,font=("goudy old style",15,"bold"),bg="light yellow").place(x=600,y=270,width=180)
        
        # button ==================
        btm_save=Button(self.dk,text="Save",command=self.add,font=("goudy old style",15,"bold"),bg="deep pink",fg="white",cursor="hand2").place(x=500,y=305,width=110,height=28)
        btm_update=Button(self.dk,text="Update",command=self.update,font=("goudy old style",15,"bold"),bg="forest green",fg="white",cursor="hand2").place(x=620,y=305,width=110,height=28)
        btm_delet=Button(self.dk,text="Delet",command=self.delete,font=("goudy old style",15,"bold"),bg="purple1",fg="white",cursor="hand2").place(x=740,y=305,width=110,height=28)
        btm_clear=Button(self.dk,text="Clear",command=self.clear,font=("goudy old style",15,"bold"),bg="blue2",fg="white",cursor="hand2").place(x=860,y=305,width=110,height=28)

        # employee detelais=====
        emp_frame=Frame(self.dk,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=150)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.employeeTabel=ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj","password","userType","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.employeeTabel.xview)
        scrolly.config(command=self.employeeTabel.yview)
        self.employeeTabel.heading("eid",text="emp ID")
        self.employeeTabel.heading("name",text="Name")
        self.employeeTabel.heading("email",text="Email")
        self.employeeTabel.heading("gender",text="Gender")
        self.employeeTabel.heading("contact",text="Contact")
        self.employeeTabel.heading("dob",text="D.O.B")
        self.employeeTabel.heading("doj",text="D.O.J")
        self.employeeTabel.heading("password",text="Password")
        self.employeeTabel.heading("userType",text="User Type")
        self.employeeTabel.heading("address",text="Address")
        self.employeeTabel.heading("salary",text="Salary")
        self.employeeTabel["show"]="headings"
        

        self.employeeTabel.column("eid",width=90)
        self.employeeTabel.column("name",width=100)
        self.employeeTabel.column("email",width=100)
        self.employeeTabel.column("gender",width=100)
        self.employeeTabel.column("contact",width=100)
        self.employeeTabel.column("dob",width=100)
        self.employeeTabel.column("doj",width=100)
        self.employeeTabel.column("password",width=100)
        self.employeeTabel.column("userType",width=100)
        self.employeeTabel.column("address",width=100)
        self.employeeTabel.column("salary",width=100)
        self.employeeTabel.pack(fill=BOTH,expand=1)
        self.employeeTabel.bind("<ButtonRelease-1>",self.get_data)
        

        self.show()
#=========================================================
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
                    cur.execute("Insert into employee (eid,name,email,gender,contact,dob,doj,password,userType,address,salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
                    self.var_emp_id.get(),
                    self.var_emp_name.get(),
                    self.var_emp_email.get(),
                    self.var_emp_gender.get(),
                    self.var_emp_contact.get(),
                    self.var_emp_dob.get(),
                    self.var_emp_doj.get(),
                    self.var_emp_password.get(),
                    self.var_emp_userType.get(),
                    self.text_address.get('1.0',END),
                    self.var_emp_salary.get()
                    ))
                    con.commit()
                    messagebox.showinfo("success","employee added successfully",parent=self.dk)
                    self.show()
        except Exception as ex:
            messagebox.showerror("error",f"error due to : {str(ex)}",parent=self.dk)

    def show(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from employee")
            rows=cur.fetchall()
            self.employeeTabel.delete(*self.employeeTabel.get_children())
            for row in rows:
                self.employeeTabel.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("error",f"error due to : {str(ex)}",parent=self.dk)

    def get_data(self,ev):
        f=self.employeeTabel.focus()
        content=(self.employeeTabel.item(f))
        row=content['values']
        # print(row)
        self.var_emp_id.set(row[0])
        self.var_emp_name.set(row[1])
        self.var_emp_email.set(row[2])
        self.var_emp_gender.set(row[3])
        self.var_emp_contact.set(row[4])
        self.var_emp_dob.set(row[5])
        self.var_emp_doj.set(row[6])
        self.var_emp_password.set(row[7])
        self.var_emp_userType.set(row[8])
        self.text_address.delete('1.0',END)
        self.text_address.insert(END,row[9])
        self.var_emp_salary.set(row[10])



    def update(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("error","employee ID must be required",parent=self.dk)
            else:
                cur.execute("select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("error"," Invalid Employee ID ",parent=self.dk)
                else:
                    cur.execute("Update employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,password=?,userType=?,address=?,salary=? where eid=? ",(
                    self.var_emp_name.get(),
                    self.var_emp_email.get(),
                    self.var_emp_gender.get(),
                    self.var_emp_contact.get(),
                    self.var_emp_dob.get(),
                    self.var_emp_doj.get(),
                    self.var_emp_password.get(),
                    self.var_emp_userType.get(),
                    self.text_address.get('1.0',END),
                    self.var_emp_salary.get(),
                    self.var_emp_id.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee Update Successfully",parent=self.dk)
                    self.show()
        except Exception as ex:
            messagebox.showerror("error",f"error due to : {str(ex)}",parent=self.dk)


    def delete(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("error","employee ID must be required",parent=self.dk)
            else:
                cur.execute("select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("error"," Invalid Employee ID ",parent=self.dk)
                else:
                    op=messagebox.askyesno("Confirm","Do you really wnat to delet?",parent=self.dk)
                    if op==True:
                        cur.execute("delete from employee where eid=?",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Success","Employee Deleted Successfully",parent=self.dk)
                        # self.show()
                        self.clear()


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
        self.var_emp_userType.set("Admin")
        self.text_address.delete('1.0',END)
        # self.text_address.insert(END,row[9])
        self.var_emp_salary.set("")
        self.var_sarchby.set("Select")
        self.var_searchtext.set("")
        self.show()

    def search(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_sarchby.get()=="Select":
                messagebox.showerror("Error","Select Search By Option",parent=self.dk)
            elif self.var_searchtext.get()=="":
                messagebox.showerror("Error","Search Input Should be required",parent=self.dk)

            else:
                cur.execute("select * from employee where "+self.var_sarchby.get()+" LIKE '%"+self.var_searchtext.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.employeeTabel.delete(*self.employeeTabel.get_children())
                    for row in rows:
                        self.employeeTabel.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record fund",parent=self.dk)


        except Exception as ex:
            messagebox.showerror("error",f"error due to : {str(ex)}",parent=self.dk)
            
if __name__=="__main__":
    dk=Tk()
    obj=employeeClass(dk)
    dk.mainloop()