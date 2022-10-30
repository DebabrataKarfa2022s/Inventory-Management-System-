from tkinter import*
# from PIL import Image,ImageTk
from tkinter import ttk ,messagebox
import sqlite3
# dk=Tk()
class categoryClass:
    def __init__(self,dk):
        self.dk=dk
        self.dk.geometry("1100x500+220+130")
        self.dk.title("Inventory Management System  | by dk")
        self.dk.config(bg="white")
        self.dk.focus_force()
# ===============Variable=================
        self.var_cat_id=StringVar()
        self.var_cat_name=StringVar()

# ===============title========================
        lbl_title=Label(self.dk,text="Manage Product Category",bd=3,relief=RIDGE,bg="turquoise1",fg="white",font=("goudy old style",30,"bold"))
        lbl_title.pack(side=TOP,fill=X,padx=10,pady=20)

        lbl_title=Label(self.dk,text="Enter Category Name",bg="white",font=("goudy old style",30))
        lbl_title.place(x=50,y=100)

        txt_name=Entry(self.dk,textvariable=self.var_cat_name,bg="light yellow",font=("goudy old style",18))
        txt_name.place(x=50,y=170,width=300)
# =========================buttom======================

        btn_add=Button(self.dk,text="ADD",command=self.add,bd=3,relief=RIDGE,fg="white",bg="red",cursor="hand2",font=("goudy old style",15))
        btn_add.place(x=360,y=170,width=150,height=30)

        btn_delete=Button(self.dk,text="Delete",command=self.delete,bd=3,relief=RIDGE,fg="white",bg="green",cursor="hand2",font=("goudy old style",15))
        btn_delete.place(x=520,y=170,width=150,height=30)

# ================== category detelais=====
        cat_frame=Frame(self.dk,bd=3,relief=RIDGE)
        cat_frame.place(x=700,y=100,width=350,height=100)

        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)

        self.catTable=ttk.Treeview(cat_frame,columns=("cid","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.catTable.xview)
        scrolly.config(command=self.catTable.yview)

        self.catTable.heading("cid",text="C ID")
        self.catTable.heading("name",text="Name")
        
        self.catTable["show"]="headings"
        

        self.catTable.column("cid",width=90)
        self.catTable.column("name",width=100)
        
        self.catTable.pack(fill=BOTH,expand=1)
        self.catTable.bind("<ButtonRelease-1>",self.get_data)
        

# =================images=================
        self.im1=PhotoImage(file="images/cat3.png")
        self.image1=Label(self.dk,image=self.im1,bd=2,relief=RAISED)
        self.image1.place(x=50,y=230)

        self.im2=PhotoImage(file="images/category1.png")
        self.image2=Label(self.dk,image=self.im2,bd=2,relief=RAISED)
        self.image2.place(x=580,y=230)

        self.show()



# ===============function============buttom==============database=========
    def add(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_cat_name.get()=="":
                messagebox.showerror("error","Category name must be required",parent=self.dk)
            else:
                cur.execute("select * from category where name=?",(self.var_cat_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("error","this category already prasent ,try another",parent=self.dk)
                else:
                    cur.execute("Insert into category (name) values(?)",(
                    self.var_cat_name.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("success","Category added successfully",parent=self.dk)
                    self.show()
        except Exception as ex:
            messagebox.showerror("error",f"error due to : {str(ex)}",parent=self.dk)

    def show(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from category")
            rows=cur.fetchall()
            self.catTable.delete(*self.catTable.get_children())
            for row in rows:
                self.catTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("error",f"error due to : {str(ex)}",parent=self.dk)


    def get_data(self,ev):
        f=self.catTable.focus()
        content=(self.catTable.item(f))
        row=content['values']
        # print(row)
        self.var_cat_id.set(row[0])
        self.var_cat_name.set(row[1])

    def delete(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_cat_id.get()=="":
                messagebox.showerror("error","Please! select category name from the list ",parent=self.dk)
            else:
                cur.execute("select * from category where cid=?",(self.var_cat_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("error"," Error,please try again ",parent=self.dk)
                else:
                    op=messagebox.askyesno("Confirm","Do you really wnat to delet?",parent=self.dk)
                    if op==True:
                        cur.execute("delete from category where cid=?",(self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Success","Category Deleted Successfully",parent=self.dk)
                        self.show()
                        self.var_cat_id.set("")
                        self.var_cat_name.set("")

        except Exception as ex:
            messagebox.showerror("error",f"error due to : {str(ex)}",parent=self.dk)



if __name__=="__main__":
    dk=Tk()
    obj=categoryClass(dk)
    dk.mainloop()