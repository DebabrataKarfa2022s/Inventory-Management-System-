from tkinter import*
# from PIL import Image,ImageTk
from tkinter import ttk ,messagebox
import sqlite3
import os
# dk=Tk()
class salesClass:
    def __init__(self,dk):
        self.dk=dk
        self.dk.geometry("1100x500+220+130")
        self.dk.title("Inventory Management System  | by dk")
        self.dk.config(bg="white")
        self.dk.focus_force()
# ******************************************************************************
# ===================all variable=================
        self.var_sale_invoice=StringVar()
        self.bill_list=[]
        # ===============title========================
        lbl_title=Label(self.dk,text="View Customer Bills",bd=3,relief=RIDGE,bg="lime green",fg="white",font=("goudy old style",30,"bold"))
        lbl_title.pack(side=TOP,fill=X,padx=10,pady=20)
# ====================lable and entry==================

        lbl_invoice=Label(self.dk,text="Invoice NO",bg="white",font=("goudy old style",15))
        lbl_invoice.place(x=50,y=100)
        text_invoice=Entry(self.dk,textvariable=self.var_sale_invoice,font=("goudy old style",15,"bold"),bg="azure2").place(x=180,y=100,width=180,height=28)

# =====================search and clear button ==========================
        btm_sarch=Button(self.dk,text="Sarch",command=self.search,font=("goudy old style",15,"bold"),bg="deep pink",fg="white",cursor="hand2").place(x=370,y=100,width=120,height=28)
        btm_clear=Button(self.dk,text="Clear",command=self.clear,font=("goudy old style",15,"bold"),bg="cyan3",fg="white",cursor="hand2").place(x=500,y=100,width=120,height=28)
# ========================= frame ===========================================
        sales_frame=Frame(self.dk,bd=3,relief=RIDGE)
        sales_frame.place(x=50,y=140,width=200,height=330)
# ===================== Listbox and scrollbar for bill list ============================
        scrollx=Scrollbar(sales_frame,orient=HORIZONTAL)
        scrolly=Scrollbar(sales_frame,orient=VERTICAL)

        self.sales_list=Listbox(sales_frame,font=("goudy old style",15),bg="white",yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.sales_list.yview)
        self.sales_list.pack(fill=BOTH,expand=1)
        self.sales_list.bind("<ButtonRelease-1>",self.get_data)

        

# ========================bill area =======================
        bill_frame=Frame(self.dk,bd=3,relief=RIDGE)
        bill_frame.place(x=280,y=140,width=410,height=330)

        lbl_title1=Label(bill_frame,text=" Customer Bill Area",bg="orange",fg="white",font=("goudy old style",20,"bold"))
        lbl_title1.pack(side=TOP,fill=X)

        scrolly2=Scrollbar(bill_frame,orient=VERTICAL)
        self.bill_area=Text(bill_frame,bg="light yellow",yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT,fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH,expand=1)
        
# ========================= image =============================
        self.im1=PhotoImage(file="images/bill3.png")
        self.image1=Label(self.dk,image=self.im1,bd=0)
        self.image1.place(x=700,y=140)

        self.show()

# ========================= show function =========================================

    def show(self):
        del self.bill_list[:]
        self.sales_list.delete(0,END)
        # print(os.listdir('bill'))
        for i in os.listdir('bill'):
            # print(i.split('.'),i.split('.')[-1])
            if i.split('.')[-1]=='txt':
                self.sales_list.insert(END,i)
                self.bill_list.append(i.split('.')[0])

# ======================== get data function ==========================================

    def get_data(self,ev):
        index_no=self.sales_list.curselection()
        file_name=self.sales_list.get(index_no)
        # print(file_name)
        self.bill_area.delete('1.0',END)
        fp=open(f'bill/{file_name}','r')
        for i in fp:
            self.bill_area.insert(END,i)
        fp.close()

# ================================ search button data base ======================================

    def search(self):
        if self.var_sale_invoice.get()=="":
            messagebox.showerror("Error","Invoice no. Should be required",parent=self.dk)
        else:
            if self.var_sale_invoice.get() in self.bill_list:
                fp=open(f'bill/{self.var_sale_invoice.get()}.txt','r')
                self.bill_area.delete('1.0',END)
                for i in fp:
                    self.bill_area.insert(END,i)
                fp.close()
            else:
                messagebox.showerror("Error","Invalid invoice number",parent=self.dk)
# ============================== clear button data base ================================
    def clear(self):
        self.show()
        self.bill_area.delete('1.0',END)







if __name__=="__main__":
    dk=Tk()
    obj=salesClass(dk)
    dk.mainloop()