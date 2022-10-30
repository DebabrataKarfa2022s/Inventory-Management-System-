from tkinter import*
# from PIL import Image,ImageTk
from tkinter import ttk ,messagebox
import sqlite3
# dk=Tk()
class productClass:
    def __init__(self,dk):
        self.dk=dk
        self.dk.geometry("1100x500+220+130")
        self.dk.title("Inventory Management System  | by dk")
        self.dk.config(bg="white")
        self.dk.focus_force()
# ***************************************************************

# ==========================all variable==============
        self.var_sarchby=StringVar()
        self.var_searchtext=StringVar()

        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()
        

        self.var_pro_id=StringVar()
        self.var_pro_cat=StringVar()
        self.var_pro_sup=StringVar()
        self.var_pro_name=StringVar()
        self.var_pro_price=StringVar()
        self.var_pro_qty=StringVar()
        self.var_pro_status=StringVar()
# ================================main category frame1=====================
        product_frame=Frame(self.dk,bd=2,relief=RIDGE,bg="white")
        product_frame.place(x=10,y=10,width=450,height=480)

#========================title ====
        title=Label(product_frame,text="Manage Product Details",font=("goudy old style",15,"bold"),bg="cyan4",fg="white").pack(side=TOP,fill=X)
# ======================naming lable============
        lbl_category=Label(product_frame,text="Category",font=("goudy old style",18),bg="white").place(x=30,y=60)
        lbl_supplier=Label(product_frame,text="Supplier",font=("goudy old style",18),bg="white").place(x=30,y=110)
        lbl_product=Label(product_frame,text="Name",font=("goudy old style",18),bg="white").place(x=30,y=160)
        lbl_price=Label(product_frame,text="Price",font=("goudy old style",18),bg="white").place(x=30,y=210)
        lbl_quantity=Label(product_frame,text="Quantity",font=("goudy old style",18),bg="white").place(x=30,y=260)
        lbl_status=Label(product_frame,text="Status",font=("goudy old style",18),bg="white").place(x=30,y=310)
# ================naming entry and combobox ===========================

        cmb_category=ttk.Combobox(product_frame,textvariable=self.var_pro_cat,values=self.cat_list,state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_category.place(x=150,y=60,width=200)
        cmb_category.current(0)

        cmb_supplier=ttk.Combobox(product_frame,textvariable=self.var_pro_sup,values=self.sup_list,state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_supplier.place(x=150,y=110,width=200)
        cmb_supplier.current(0)

        text_name=Entry(product_frame,textvariable=self.var_pro_name,font=("goudy old style",15,"bold"),bg="light yellow").place(x=150,y=160,width=200)
        text_price=Entry(product_frame,textvariable=self.var_pro_price,font=("goudy old style",15,"bold"),bg="light yellow").place(x=150,y=210,width=200)
        text_qty=Entry(product_frame,textvariable=self.var_pro_qty,font=("goudy old style",15,"bold"),bg="light yellow").place(x=150,y=260,width=200)

        cmb_status=ttk.Combobox(product_frame,textvariable=self.var_pro_status,values=("Active","Inactive"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_status.place(x=150,y=310,width=200)
        cmb_status.current(0)
# ===================all buttom for frame1 =========================

        btm_save=Button(product_frame,text="Save",command=self.add,font=("goudy old style",15,"bold"),bg="dark turquoise",fg="white",cursor="hand2").place(x=10,y=400,width=100,height=40)
        btm_update=Button(product_frame,text="Update",command=self.update,font=("goudy old style",15,"bold"),bg="yellow4",fg="white",cursor="hand2").place(x=120,y=400,width=100,height=40)
        btm_delet=Button(product_frame,text="Delete",command=self.delete,font=("goudy old style",15,"bold"),bg="springGreen2",fg="white",cursor="hand2").place(x=230,y=400,width=100,height=40)
        btm_clear=Button(product_frame,text="Clear",command=self.clear,font=("goudy old style",15,"bold"),bg="maroon1",fg="white",cursor="hand2").place(x=340,y=400,width=100,height=40)
# =================== sarchframe ========================
        sarchframe=LabelFrame(self.dk,text="Serch Product",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        sarchframe.place(x=480,y=10,width=600,height=80)
        # option====
        cmb_sarch=ttk.Combobox(sarchframe,textvariable=self.var_sarchby,values=("Select","Category","Supplier","Name"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_sarch.place(x=10,y=10,width=180)
        cmb_sarch.current(0)

        text_sarch=Entry(sarchframe,textvariable=self.var_searchtext,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btm_sarch=Button(sarchframe,text="Search",command=self.search,font=("goudy old style",15,"bold"),bg="purple4",fg="white",cursor="hand2").place(x=420,y=9,width=150,height=30)
# ============= treview and product details========================

        p_frame=Frame(self.dk,bd=3,relief=RIDGE)
        p_frame.place(x=480,y=100,width=600,height=400)

        scrolly=Scrollbar(p_frame,orient=VERTICAL)
        scrollx=Scrollbar(p_frame,orient=HORIZONTAL)

        self.productTable=ttk.Treeview(p_frame,columns=("pid","Category","Supplier","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.productTable.xview)
        scrolly.config(command=self.productTable.yview)
        self.productTable.heading("pid",text="Pro ID")
        self.productTable.heading("Category",text="Category")
        self.productTable.heading("Supplier",text="Supplier")
        self.productTable.heading("name",text="Name")
        self.productTable.heading("price",text="Price")
        self.productTable.heading("qty",text="Qty")
        self.productTable.heading("status",text="Status")
        
        self.productTable["show"]="headings"
        

        self.productTable.column("pid",width=90)
        self.productTable.column("Category",width=100)
        self.productTable.column("Supplier",width=100)
        self.productTable.column("name",width=100)
        self.productTable.column("price",width=100)
        self.productTable.column("qty",width=100)
        self.productTable.column("status",width=100)

        self.productTable.pack(fill=BOTH,expand=1)
        self.productTable.bind("<ButtonRelease-1>",self.get_data)
        

        self.show()
        

#========================buttom data base =================================

    def fetch_cat_sup(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        self.cat_list.append("Empty")
        self.sup_list.append("Empty")
        try:
            cur.execute("select name from category")
            cat=cur.fetchall()
            # print(cat)
            # cat_list=[]
            
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])
            # print(self.cat_list)

            cur.execute("select name from supplier")
            sup=cur.fetchall()
            # print(sup)
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])


        except Exception as ex:
            messagebox.showerror("error",f"error due to : {str(ex)}",parent=self.dk)





    def add(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_pro_cat.get()=="Select" or self.var_pro_cat.get()=="Empty" or self.var_pro_sup.get()=="Select" or self.var_pro_name.get()=="":
                messagebox.showerror("error","All fields are required",parent=self.dk)
            else:
                cur.execute("select * from product where name=?",(self.var_pro_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("error","Product already prasent ,try another",parent=self.dk)
                else:
                    cur.execute("Insert into product (Category,Supplier,name,price,qty,status) values(?,?,?,?,?,?)",(
                    self.var_pro_cat.get(),
                    self.var_pro_sup.get(),
                    self.var_pro_name.get(),
                    self.var_pro_price.get(),
                    self.var_pro_qty.get(),
                    self.var_pro_status.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("success","Product added successfully",parent=self.dk)
                    self.show()
        except Exception as ex:
            messagebox.showerror("error",f"error due to : {str(ex)}",parent=self.dk)

    def show(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            rows=cur.fetchall()
            self.productTable.delete(*self.productTable.get_children())
            for row in rows:
                self.productTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("error",f"error due to : {str(ex)}",parent=self.dk)

    def get_data(self,ev):
        f=self.productTable.focus()
        content=(self.productTable.item(f))
        row=content['values']
        # print(row)
        self.var_pro_id.set(row[0])
        self.var_pro_cat.set(row[1])
        self.var_pro_sup.set(row[2])
        self.var_pro_name.set(row[3])
        self.var_pro_price.set(row[4])
        self.var_pro_qty.set(row[5])
        self.var_pro_status.set(row[6])


    def update(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_pro_id.get()=="":
                messagebox.showerror("error","please select product from list",parent=self.dk)
            else:
                cur.execute("select * from product where pid=?",(self.var_pro_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("error"," Invalid Product  ",parent=self.dk)
                else:
                    cur.execute("Update Product set Category=?,Supplier=?,name=?,price=?,qty=?,status=? where pid=? ",(
                    self.var_pro_cat.get(),
                    self.var_pro_sup.get(),
                    self.var_pro_name.get(),
                    self.var_pro_price.get(),
                    self.var_pro_qty.get(),
                    self.var_pro_status.get(),
                    self.var_pro_id.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Product Update Successfully",parent=self.dk)
                    self.show()
        except Exception as ex:
            messagebox.showerror("error",f"error due to : {str(ex)}",parent=self.dk)


    def delete(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_pro_id.get()=="":
                messagebox.showerror("error","please select product from the list",parent=self.dk)
            else:
                cur.execute("select * from product where pid=?",(self.var_pro_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("error"," Invalid Product ",parent=self.dk)
                else:
                    op=messagebox.askyesno("Confirm","Do you really wnat to delet?",parent=self.dk)
                    if op==True:
                        cur.execute("delete from product where pid=?",(self.var_pro_id.get(),))
                        con.commit()
                        messagebox.showinfo("Success","Product Deleted Successfully",parent=self.dk)
                        self.show()
                        # self.clear()


        except Exception as ex:
            messagebox.showerror("error",f"error due to : {str(ex)}",parent=self.dk)

    def clear(self):
        self.var_pro_id.set("")
        self.var_pro_cat.set("Select")
        self.var_pro_sup.set("Select")
        self.var_pro_name.set("")
        self.var_pro_price.set("")
        self.var_pro_qty.set("")
        self.var_pro_status.set("Active")
        
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
                cur.execute("select * from product where "+self.var_sarchby.get()+" LIKE '%"+self.var_searchtext.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.productTable.delete(*self.productTable.get_children())
                    for row in rows:
                        self.productTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record fund",parent=self.dk)


        except Exception as ex:
            messagebox.showerror("error",f"error due to : {str(ex)}",parent=self.dk)
            



if __name__=="__main__":
    dk=Tk()
    obj=productClass(dk)
    dk.mainloop()