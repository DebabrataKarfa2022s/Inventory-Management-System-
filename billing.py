from tkinter import*
# from PIL import Image,ImageTk
from tkinter import ttk , messagebox
import sqlite3
import time
import os
import tempfile


# dk=Tk()
class billClass:
    def __init__(self,dk):
        self.dk=dk
        self.dk.geometry("1350x700+0+0")
        self.dk.title("Inventory Management System  | by dk")
        self.dk.config(bg="white")
# ============================all variable =========================
        self.var_bill_search=StringVar()
        self.var_bill_name=StringVar()
        self.var_bill_contact=StringVar()
        self.var_bill_Cname=StringVar()
        self.var_bill_pid=StringVar()
        self.var_bill_price=StringVar()
        self.var_bill_qty=StringVar()
        self.var_bill_stock=StringVar()
        self.var_bill_cal_input=StringVar()
        self.cart_list=[]
        self.chk_print=0



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

# ================== product frame ================================
        pro_frame=Frame(self.dk,bd=3,relief=RIDGE,bg="white")
        pro_frame.place(x=6,y=110,width=410,height=550)

        pro_title=Label(pro_frame,text="All Product",font=("goudy old style",20,"bold"),bg="springGreen2",fg="white").pack(side=TOP,fill=X)

        pro_frame1=Frame(pro_frame,bd=2,relief=RIDGE,bg="white")
        pro_frame1.place(x=2,y=42,width=398,height=90)

        lbl_search=Label(pro_frame1,text="Search Product | By Name",font=("times new roman",15,"bold"),bg="white",fg="deep sky blue").place(x=2,y=5)

        lbl_name=Label(pro_frame1,text="Product Name",font=("times new roman",15,"bold"),bg="white").place(x=5,y=45)

        txt_search=Entry(pro_frame1,textvariable=self.var_bill_search,font=("times new roman",15),bg="light yellow").place(x=135,y=47,width=150,height=22)

        btm_search=Button(pro_frame1,text="Search",command=self.search,font=("goudy old style",15,"bold"),bg="deep pink",fg="white",cursor="hand2").place(x=288,y=45,width=100,height=25)
        btm_show_all=Button(pro_frame1,text="Show All",command=self.show,font=("goudy old style",15,"bold"),bg="salmon",fg="white",cursor="hand2").place(x=288,y=10,width=110,height=28)

# =================================== product Details frame =======================


        product_frame2=Frame(pro_frame,bd=3,relief=RIDGE)
        product_frame2.place(x=2,y=140,width=398,height=375)

        scrolly=Scrollbar(product_frame2,orient=VERTICAL)
        scrollx=Scrollbar(product_frame2,orient=HORIZONTAL)

        self.productTable=ttk.Treeview(product_frame2,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.productTable.xview)
        scrolly.config(command=self.productTable.yview)

        self.productTable.heading("pid",text="P.ID")
        self.productTable.heading("name",text="Name")
        self.productTable.heading("price",text="Price")
        self.productTable.heading("qty",text="Qty")
        self.productTable.heading("status",text="Status")
        
        self.productTable["show"]="headings"
        

        self.productTable.column("pid",width=40)
        self.productTable.column("name",width=100)
        self.productTable.column("price",width=100)
        self.productTable.column("qty",width=40)
        self.productTable.column("status",width=100)
        
        self.productTable.pack(fill=BOTH,expand=1)
        self.productTable.bind("<ButtonRelease-1>",self.get_data)

        lbl_note=Label(pro_frame,text="'Note', 'Enter 0 Quantity to remove product from the cart' ",font=("goudy old style",12),fg="red",bg="white").pack(side=BOTTOM,fill=X)

# ===============================customer frame =====================================================================================================================================================================

        customer_frame=Frame(self.dk,bd=3,relief=RIDGE)
        customer_frame.place(x=420,y=110,width=530,height=70)

        customer_title=Label(customer_frame,text="Customer Details",compound=LEFT,font=("times new roman",15,"bold"),bg="bisque2")
        customer_title.pack(side=TOP,fill=X)

        lbl_name=Label(customer_frame,text="Name",font=("times new roman",15),bg="white").place(x=5,y=35)
        txt_name=Entry(customer_frame,textvariable=self.var_bill_name,font=("times new roman",12),bg="light yellow").place(x=80,y=35,width=180)

        lbl_contact=Label(customer_frame,text="Contact",font=("times new roman",15),bg="white").place(x=280,y=35)

        txt_contact=Entry(customer_frame,textvariable=self.var_bill_contact,font=("times new roman",12),bg="light yellow").place(x=370,y=35,width=140)

# ======================= calculter and cart frame ==================
        cal_cart_frame=Frame(self.dk,bd=2,relief=RIDGE)
        cal_cart_frame.place(x=420,y=190,width=530,height=360)
        
# ========================= calculeter frame===================================
        cal_frame=Frame(cal_cart_frame,bd=8,relief=RIDGE)
        cal_frame.place(x=5,y=10,width=268,height=340)

        txt_cal_input=Entry(cal_frame,textvariable=self.var_bill_cal_input,font=("arial",15,"bold"),width=21,bd=10,relief=GROOVE,justify=RIGHT,bg="cyan2")
        txt_cal_input.grid(row=0,columnspan=4)

        btn_7=Button(cal_frame,text=7,command=lambda:self.get_input(7),font=('airal',15,"bold"),bd=5,width=4,pady=10,cursor="hand2",bg="cyan2").grid(row=1,column=0)
        btn_8=Button(cal_frame,text=8,command=lambda:self.get_input(8),font=('airal',15,"bold"),bd=5,width=4,pady=10,cursor="hand2",bg="cyan2").grid(row=1,column=1)
        btn_9=Button(cal_frame,text=9,command=lambda:self.get_input(9),font=('airal',15,"bold"),bd=5,width=4,pady=10,cursor="hand2",bg="cyan2").grid(row=1,column=2)
        btn_sum=Button(cal_frame,text="+",command=lambda:self.get_input('+'),font=('airal',15,"bold"),bd=5,width=4,pady=10,cursor="hand2",bg="cyan2").grid(row=1,column=3)

        btn_4=Button(cal_frame,text=4,command=lambda:self.get_input(4),font=('airal',15,"bold"),bd=5,width=4,pady=10,cursor="hand2",bg="cyan2").grid(row=2,column=0)
        btn_5=Button(cal_frame,text=5,command=lambda:self.get_input(5),font=('airal',15,"bold"),bd=5,width=4,pady=10,cursor="hand2",bg="cyan2").grid(row=2,column=1)
        btn_6=Button(cal_frame,text=6,command=lambda:self.get_input(6),font=('airal',15,"bold"),bd=5,width=4,pady=10,cursor="hand2",bg="cyan2").grid(row=2,column=2)
        btn_substract=Button(cal_frame,command=lambda:self.get_input('-'),text="-",font=('airal',15,"bold"),bd=5,width=4,pady=10,cursor="hand2",bg="cyan2").grid(row=2,column=3)

        btn_1=Button(cal_frame,text=1,command=lambda:self.get_input(1),font=('airal',15,"bold"),bd=5,width=4,pady=10,cursor="hand2",bg="cyan2").grid(row=3,column=0)
        btn_2=Button(cal_frame,text=2,command=lambda:self.get_input(2),font=('airal',15,"bold"),bd=5,width=4,pady=10,cursor="hand2",bg="cyan2").grid(row=3,column=1)
        btn_3=Button(cal_frame,text=3,command=lambda:self.get_input(3),font=('airal',15,"bold"),bd=5,width=4,pady=10,cursor="hand2",bg="cyan2").grid(row=3,column=2)
        btn_multiplication=Button(cal_frame,text="*",command=lambda:self.get_input('*'),font=('airal',15,"bold"),bd=5,width=4,pady=10,cursor="hand2",bg="cyan2").grid(row=3,column=3)

        btn_0=Button(cal_frame,text=0,command=lambda:self.get_input(0),font=('airal',15,"bold"),bd=5,width=4,pady=15,cursor="hand2",bg="cyan2").grid(row=4,column=0)
        btn_c=Button(cal_frame,text="C",command=self.clear_cal,font=('airal',15,"bold"),bd=5,width=4,pady=15,cursor="hand2",bg="cyan2").grid(row=4,column=1)
        btn_equal=Button(cal_frame,text="=",command=self.perform_cal,font=('airal',15,"bold"),bd=5,width=4,pady=15,cursor="hand2",bg="cyan2").grid(row=4,column=2)
        btn_division=Button(cal_frame,text="/",command=lambda:self.get_input('/'),font=('airal',15,"bold"),bd=5,width=4,pady=15,cursor="hand2",bg="cyan2").grid(row=4,column=3)


# ========================== cart frame ======================================

        cart_frame=Frame(cal_cart_frame,bd=3,relief=RIDGE)
        cart_frame.place(x=280,y=8,width=245,height=342)

        self.lbl_cart=Label(cart_frame,text="Cart\tTotal Product : [0]",font=("times new roman",15),bg="violetRed3")
        self.lbl_cart.pack(side=TOP,fill=X)

        
        scrolly=Scrollbar(cart_frame,orient=VERTICAL)
        scrollx=Scrollbar(cart_frame,orient=HORIZONTAL)

        self.cartTable=ttk.Treeview(cart_frame,columns=("pid","name","price","qty"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.cartTable.xview)
        scrolly.config(command=self.cartTable.yview)

        self.cartTable.heading("pid",text="P.ID")
        self.cartTable.heading("name",text="Name")
        self.cartTable.heading("price",text="Price")
        self.cartTable.heading("qty",text="Qty")
        # self.cartTable.heading("status",text="Status")
        
        self.cartTable["show"]="headings"
        

        self.cartTable.column("pid",width=40)
        self.cartTable.column("name",width=100)
        self.cartTable.column("price",width=90)
        self.cartTable.column("qty",width=40)
        # self.cartTable.column("status",width=90)
        
        self.cartTable.pack(fill=BOTH,expand=1)
        self.cartTable.bind("<ButtonRelease-1>",self.get_data_cart)




# ============================ ADD cart frame  ======================
        Add_cart_frame=Frame(self.dk,bd=2,relief=RIDGE)
        Add_cart_frame.place(x=420,y=550,width=530,height=110)

        lbl_product_name=Label(Add_cart_frame,text="Product Name",font=("times new roman",15)).place(x=5,y=5)
        txt_product_name=Entry(Add_cart_frame,textvariable=self.var_bill_Cname,font=("times new roman",15),bg="light yellow",state='readonly').place(x=5,y=35,width=190,height=24)

        lbl_product_price=Label(Add_cart_frame,text="Price per Qty",font=("times new roman",15)).place(x=230,y=5)
        txt_product_price=Entry(Add_cart_frame,textvariable=self.var_bill_price,font=("times new roman",15),bg="light yellow",state='readonly').place(x=230,y=35,width=150,height=24)

        lbl_product_qty=Label(Add_cart_frame,text="Quantity",font=("times new roman",15)).place(x=390,y=5)
        txt_product_qty=Entry(Add_cart_frame,textvariable=self.var_bill_qty,font=("times new roman",15),bg="light yellow").place(x=390,y=35,width=120,height=24)

        self.lbl_product_inStock=Label(Add_cart_frame,text="In Stock",font=("times new roman",15))
        self.lbl_product_inStock.place(x=5,y=70)

        btn_clear_cart=Button(Add_cart_frame,text="Clear",command=self.clear_cart,font=("times new roman",16,"bold"),bg="magenta4",cursor="hand2")
        btn_clear_cart.place(x=180,y=70,height=30,width=150)

        btn__add_cart=Button(Add_cart_frame,command=self.add_update_cart,text="Add | Update Cart",font=("times new roman",16,"bold"),bg="yellow",cursor="hand2",background="red")
        btn__add_cart.place(x=340,y=70,height=30,width=180)


# =============================== billings area =====================================================================
        bill_frame=Frame(self.dk,bd=2,relief=RIDGE,bg="white")
        bill_frame.place(x=953,y=110,width=400,height=410)

        billing_title=Label(bill_frame,text="Customer Billing Area",font=("goudy old style",20,"bold"),bg="gold3",fg="white").pack(side=TOP,fill=X)

        scrolly=Scrollbar(bill_frame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)

        self.txt_bill_area=Text(bill_frame,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)

        scrolly.config(command=self.txt_bill_area.yview)
        # =========================== billing Button ================================
        bill_menu_frame=Frame(self.dk,bd=2,relief=RIDGE,bg="white")
        bill_menu_frame.place(x=953,y=520,width=400,height=140)

        self.lbl_amaunt=Label(bill_menu_frame,text="Bill Amount\n[0]",font=("goudy old style",15,"bold"),bg="orange red",fg="white")
        self.lbl_amaunt.place(x=2,y=5,width=138,height=70)

        self.lbl_discount=Label(bill_menu_frame,text="Discount \n[5%]",font=("goudy old style",15,"bold"),bg="slate Blue4",fg="white")
        self.lbl_discount.place(x=144,y=5,width=120,height=70)

        self.lbl_net_pay=Label(bill_menu_frame,text="Net Pay\n[0]",font=("goudy old style",15,"bold"),bg="Light Blue4",fg="white")
        self.lbl_net_pay.place(x=268,y=5,width=126,height=70)


        btn_print=Button(bill_menu_frame,text="Print",command=self.print_bill,font=("times new roman",15,"bold"),bg="light goldenrod",cursor="hand2")
        btn_print.place(x=2,y=80,height=50,width=120)

        btn_clear_all=Button(bill_menu_frame,text="Clear All",command=self.clear_all,font=("times new roman",15,"bold"),bg="dodger blue",cursor="hand2")
        btn_clear_all.place(x=126,y=80,height=50,width=132)

        btn_generate=Button(bill_menu_frame,text="Generate Bill",command=self.generate_bill,font=("times new roman",15,"bold"),bg="yellow3",cursor="hand2")
        btn_generate.place(x=264,y=80,height=50,width=126)

# =========================== footer ======================================================
        footer=Label(self.dk,text="Inventory Management System |developed  by dk \n any problem contact 8436832600",font=("goudy old style",10),bg="Olive Drab1").pack(side=BOTTOM,fill=X)

        self.show()
        # self.bill_top()
        self.update_date_time()

# ==================================== all function for calculeter ============================================================
    def get_input(self,num):
        xnum=self.var_bill_cal_input.get()+str(num)
        self.var_bill_cal_input.set(xnum)
    def clear_cal(self):
        self.var_bill_cal_input.set('')
    def perform_cal(self):
        result=self.var_bill_cal_input.get()
        self.var_bill_cal_input.set(eval(result))

# ============================================

    def show(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
 
        try:
            cur.execute("select pid,name,price,qty,status from product where status='Active'")
            rows=cur.fetchall()
            self.productTable.delete(*self.productTable.get_children())
            for row in rows:
                self.productTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("error",f"error due to : {str(ex)}",parent=self.dk)


    def search(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            
            if self.var_bill_search.get()=="":
                messagebox.showerror("Error","Search Input Should be required",parent=self.dk)

            else:
                cur.execute("select pid,name,price,qty,status from product where name  LIKE '%"+self.var_bill_search.get()+"%' and status='Active' ")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.productTable.delete(*self.productTable.get_children())
                    for row in rows:
                        self.productTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record fund",parent=self.dk)


        except Exception as ex:
            messagebox.showerror("error",f"error due to : {str(ex)}",parent=self.dk)
            
    def get_data(self,ev):
        f=self.productTable.focus()
        content=(self.productTable.item(f))
        row=content['values']
        # print(row)
        self.var_bill_pid.set(row[0])
        self.var_bill_Cname.set(row[1])
        self.var_bill_price.set(row[2])
        # self.var_bill_stock.set(row[4])
        self.lbl_product_inStock.config(text=f"In Stock [{str(row[3])}]")
        self.var_bill_stock.set(row[3])
        self.var_bill_qty.set('1')

    def get_data_cart(self,ev):
        f=self.cartTable.focus()
        content=(self.cartTable.item(f))
        row=content['values']
        # print(row)
        self.var_bill_pid.set(row[0])
        self.var_bill_Cname.set(row[1])
        self.var_bill_price.set(row[2])
        self.var_bill_qty.set(row[3])
        # self.var_bill_stock.set(row[4])
        self.lbl_product_inStock.config(text=f"In Stock [{str(row[4])}]")
        self.var_bill_stock.set(row[4])
        
    def add_update_cart(self):
        if self.var_bill_pid.get()=="":
            messagebox.showerror("Error","please select product from the list")
        elif self.var_bill_qty.get()=="":
            messagebox.showerror("Error","Quantity is required",parent=self.dk)

        elif int(self.var_bill_qty.get())>int(self.var_bill_stock.get()):
            messagebox.showerror("Error"," Invalid Quantity ",parent=self.dk)


        else:
            # price_cal=float(int(self.var_bill_qty.get())*float(self.var_bill_price.get()))
            price_cal=self.var_bill_price.get()
            cart_data=[self.var_bill_pid.get(),self.var_bill_Cname.get(),price_cal,self.var_bill_qty.get(),self.var_bill_stock.get()]
                # =====update cart=============
            present='no'
            index_no=0
            for row in self.cart_list:
                if self.var_bill_pid.get()==row[0]:
                    present='yes'
                    break
                index_no+=1
            if present=='yes':
                op=messagebox.askyesno("Confirm","Product already present\nDo you wnat to Update | Remove from the cart List",parent=self.dk)
                if op==True:
                    if self.var_bill_qty.get()=="0":
                        self.cart_list.pop(index_no)
                    else:
                        # self.cart_list[index_no][2]=price_cal
                        self.cart_list[index_no][3]=self.var_bill_qty.get()
            else:    
                self.cart_list.append(cart_data)
            self.show_cart()
            self.bill_update()

    def bill_update(self):
        self.bill_amount=0
        self.net_pay=0
        self.discount=0
        for row in self.cart_list:
           self.bill_amount=self.bill_amount+((float(row[2]))*int(row[3]))
        self.discount=(self.bill_amount*5)/100
        self.net_pay=self.bill_amount-(self.bill_amount*5)/100
        self.lbl_amaunt.config(text=f'Bill Amount(Rs.)\n[{str(self.bill_amount)}]')
        self.lbl_net_pay.config(text=f'Net Pay(Rs.)\n[{str(self.net_pay)}]')
        self.lbl_cart.config(text=f"Cart\t Total Product:[{(len(self.cart_list))}]")

    def show_cart(self):
        try:
            self.cartTable.delete(*self.cartTable.get_children())
            for row in self.cart_list:
                self.cartTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("error",f"error due to : {str(ex)}",parent=self.dk)


    def generate_bill(self):
        if self.var_bill_name.get()=='' or self.var_bill_contact.get()=='':
            messagebox.showerror("Error",f"Customer Details are required",parent=self.dk)
        elif len(self.cart_list)==0:
            messagebox.showerror("Error",f"Please Add Product to the cart!!",parent=self.dk)
        else:
            # =====bill top=====
            self.bill_top()
            # ==================== bill middle ==========
            self.bill_middle()
            # ============ bill bottom==========
            self.bill_bottom()

            fp=open(f'bill/{str(self.invoice)}.txt','w')
            fp.write(self.txt_bill_area.get('1.0',END))
            fp.close()
            messagebox.showinfo("Saved","Bill has been generate/save in Backend",parent=self.dk)

            self.chk_print=1


    
    def bill_top(self):
        self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
        # print(self.invoice)
        bill_top_temp=f'''
\t\tXYZ-Inventory
\t Phone No.9832****** , Kolkata-700012
{str("="*46)}
Customer Name : {self.var_bill_name.get()}
Ph no : {self.var_bill_contact.get()}
Bill No. {str(self.invoice)}\t\t\tDate: {str(time.strftime("%d.%m.%Y"))}
{str("="*46)}
 Product Name\t\t\tQty\tPrice
{str("="*46)}
            '''
        self.txt_bill_area.delete('1.0',END)
        self.txt_bill_area.insert('1.0', bill_top_temp)
    

    def bill_middle(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            for row in self.cart_list:
            # pid,name,price,qty,stock
                
                pid=row[0]
                name=row[1]
                qty=int(row[4])-int(row[3])
                if int(row[3])==int(row[4]):
                    status='Inactive'
                if int(row[3])!=int(row[4]):
                    status='Active'
                price=float(row[2])*int(row[3])
                price=str(price)
                self.txt_bill_area.insert(END,"\n "+name+"\t\t\t"+row[3]+"\tRs."+price)
                # ===== update quantity in product table -=====
                cur.execute('Update product set qty=?,status=? where pid=?',(
                    qty,
                    status,
                    pid
                ))
                con.commit()
            con.close()
            self.show()
        except Exception as ex:
            messagebox.showerror("error",f"error due to : {str(ex)}",parent=self.dk)


    def bill_bottom(self):
        bill_bottom_temp=f'''
{str("="*46)}
 Bill Amount\t\t\t\tRs.{self.bill_amount}
 Discount\t\t\t\tRs.{self.discount}
 Net Pay\t\t\t\tRs.{self.net_pay}
{str("="*46)}\n
        '''
        self.txt_bill_area.insert(END, bill_bottom_temp)



    def clear_cart(self):
        self.var_bill_pid.set('')
        self.var_bill_Cname.set('')
        self.var_bill_price.set('')
        self.var_bill_qty.set('')
        # self.var_bill_stock.set(row[4])
        self.lbl_product_inStock.config(text=f"In Stock")
        self.var_bill_stock.set('')
    
    def clear_all(self):
        del self.cart_list[:]
        self.var_bill_Cname.set('')
        self.var_bill_contact.set('')
        self.txt_bill_area.delete('1.0',END)
        self.lbl_cart.config(text=f"Cart\t Total Product:[0]")
        self.var_bill_search.set('')
        self.clear_cart()
        self.show()
        self.show_cart()
        self.chk_print=0

    def update_date_time(self):
        time_in=time.strftime("%I-%M-%S")
        date_in=time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"Welcome to Inventory Management System\t\t Date:- {str(date_in)}\t\t Time:- {str(time_in)}")
        self.lbl_clock.after(200,self.update_date_time)

    def print_bill(self):
        if self.chk_print==1:
            messagebox.showinfo('print',"please wait while printing",parent=self.dk)

            new_file=tempfile.mktemp('.txt')
            open(new_file,'w').write(self.txt_bill_area.get('1.0',END))
            os.startfile(new_file,'print')
        else:
            messagebox.showerror('print',"please generate bill , to print the recipt",parent=self.dk)

    def logout(self):
        self.dk.destroy()
        os.system("python login.py")



if __name__=="__main__":
    dk=Tk()
    obj=billClass(dk)
    dk.mainloop()