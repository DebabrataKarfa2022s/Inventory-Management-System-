from tkinter import*
# from PIL import Image,ImageTk
from tkinter import ttk ,messagebox
import sqlite3
# dk=Tk()
class supplierClass:
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

        self.var_sup_invoice=StringVar()
        self.var_sup_name=StringVar()
        self.var_sup_contact=StringVar()
        
        # sarchframe===
        # option====
        lbl_sarch=Label(self.dk,text="Invoice NO",bg="white",font=("goudy old style",15))
        lbl_sarch.place(x=650,y=80)
        
        # search button 
        text_sarch=Entry(self.dk,textvariable=self.var_searchtext,font=("goudy old style",15),bg="azure2").place(x=760,y=80)
        btm_sarch=Button(self.dk,text="Sarch",command=self.search,font=("goudy old style",15,"bold"),bg="deep pink",fg="white",cursor="hand2").place(x=970,y=79,width=100,height=30)

        # title ====
        title=Label(self.dk,text="Supplier Details",font=("goudy old style",20,"bold"),bg="blue2",fg="white").place(x=50,y=10,width=1000,height=40)

        # content ===
        # row1=======
        
        lbl_supplier_invoice=Label(self.dk,text="Invoice No. ",font=("goudy old style",15,"bold"),bg="white").place(x=50,y=80)
        text_supplier_invoice=Entry(self.dk,textvariable=self.var_sup_invoice,font=("goudy old style",15,"bold"),bg="azure2").place(x=180,y=80,width=180)
        
        # row2======
        
        lbl_name=Label(self.dk,text="Name",font=("goudy old style",15,"bold"),bg="white").place(x=50,y=120)
        text_name=Entry(self.dk,textvariable=self.var_sup_name,font=("goudy old style",15,"bold"),bg="azure2").place(x=180,y=120,width=180)
        
        # row3==============

        lbl_contact=Label(self.dk,text="Contact",font=("goudy old style",15,"bold"),bg="white").place(x=50,y=160)
        text_contact=Entry(self.dk,textvariable=self.var_sup_contact,font=("goudy old style",15,"bold"),bg="azure2").place(x=180,y=160,width=180)
       

        # row4=====
        lbl_desc=Label(self.dk,text="Description",font=("goudy old style",15,"bold"),bg="white").place(x=50,y=200)
 
        self.text_desc=Text(self.dk,font=("goudy old style",15,"bold"),bg="azure2")
        self.text_desc.place(x=180,y=200,width=470,height=120)
        # button ==================
        btm_save=Button(self.dk,text="Save",command=self.add,font=("goudy old style",15,"bold"),bg="deep sky blue",fg="white",cursor="hand2").place(x=180,y=370,width=110,height=35)
        btm_update=Button(self.dk,text="Update",command=self.update,font=("goudy old style",15,"bold"),bg="DarkGoldenrod1",fg="white",cursor="hand2").place(x=300,y=370,width=110,height=35)
        btm_delet=Button(self.dk,text="Delet",command=self.delete,font=("goudy old style",15,"bold"),bg="magenta2",fg="white",cursor="hand2").place(x=420,y=370,width=110,height=35)
        btm_clear=Button(self.dk,text="Clear",command=self.clear,font=("goudy old style",15,"bold"),bg="chartreuse2",fg="white",cursor="hand2").place(x=540,y=370,width=110,height=35)

        # employee detelais=====
        emp_frame=Frame(self.dk,bd=3,relief=RIDGE)
        emp_frame.place(x=700,y=120,width=380,height=350)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.supplierTable=ttk.Treeview(emp_frame,columns=("invoice","name","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)

        self.supplierTable.heading("invoice",text="Invoice NO")
        self.supplierTable.heading("name",text="Name")
        self.supplierTable.heading("contact",text="Contact")
        self.supplierTable.heading("desc",text="Description")
        
        self.supplierTable["show"]="headings"
        

        self.supplierTable.column("invoice",width=90)
        self.supplierTable.column("name",width=100)
        self.supplierTable.column("contact",width=100)
        self.supplierTable.column("desc",width=100)
        
        self.supplierTable.pack(fill=BOTH,expand=1)
        self.supplierTable.bind("<ButtonRelease-1>",self.get_data)
        

        self.show()
#=========================================================
    def add(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("error","Invoice must be required",parent=self.dk)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("error","this Invoice no. already assigned ,try another",parent=self.dk)
                else:
                    cur.execute("Insert into supplier (invoice,name,contact,desc) values(?,?,?,?)",(
                    self.var_sup_invoice.get(),
                    self.var_sup_name.get(),
                    self.var_sup_contact.get(),
                    self.text_desc.get('1.0',END)
                    ))
                    con.commit()
                    messagebox.showinfo("success","Supplier added successfully",parent=self.dk)
                    self.show()
        except Exception as ex:
            messagebox.showerror("error",f"error due to : {str(ex)}",parent=self.dk)

    def show(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from supplier")
            rows=cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("error",f"error due to : {str(ex)}",parent=self.dk)

    def get_data(self,ev):
        f=self.supplierTable.focus()
        content=(self.supplierTable.item(f))
        row=content['values']
        # print(row)
        self.var_sup_invoice.set(row[0])
        self.var_sup_name.set(row[1])
        self.var_sup_contact.set(row[2])
        self.text_desc.delete('1.0',END)
        self.text_desc.insert(END,row[3])
        


    def update(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("error","Invoice no must be required",parent=self.dk)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("error"," Invalid Invoice no ",parent=self.dk)
                else:
                    cur.execute("Update supplier set  name=?,contact=?,desc=? where invoice=? ",(
                    self.var_sup_name.get(),
                    self.var_sup_contact.get(),
                    self.text_desc.get('1.0',END),
                    self.var_sup_invoice.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Update Successfully",parent=self.dk)
                    self.show()
        except Exception as ex:
            messagebox.showerror("error",f"error due to : {str(ex)}",parent=self.dk)


    def delete(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("error","Invoice no must be required",parent=self.dk)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("error"," Invalid supplier no ",parent=self.dk)
                else:
                    op=messagebox.askyesno("Confirm","Do you really wnat to delet?",parent=self.dk)
                    if op==True:
                        cur.execute("delete from supplier where invoice=?",(self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Success","Supplier Deleted Successfully",parent=self.dk)
                        # self.show()
                        self.clear()
        except Exception as ex:
            messagebox.showerror("error",f"error due to : {str(ex)}",parent=self.dk)

    def clear(self):
        self.var_sup_invoice.set("")
        self.var_sup_name.set("")
        self.var_sup_contact.set("")
        self.text_desc.delete('1.0',END)
        # self.text_desc.insert(END,row[9])
        
        self.var_searchtext.set("")
        self.show()

    def search(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            
            if self.var_searchtext.get()=="":
                messagebox.showerror("Error","Invoice no Should be required",parent=self.dk)

            else:
                cur.execute("select * from supplier where invoice=?",(self.var_searchtext.get(),))
                rows=cur.fetchone()
                if rows!=None:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    self.supplierTable.insert('',END,values=rows)
                else:
                    messagebox.showerror("Error","No record fund",parent=self.dk)


        except Exception as ex:
            messagebox.showerror("error",f"error due to : {str(ex)}",parent=self.dk)
            
if __name__=="__main__":
    dk=Tk()
    obj=supplierClass(dk)
    dk.mainloop()