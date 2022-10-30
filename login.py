from tkinter import*
# from PIL import ImageTk
from tkinter import messagebox
import sqlite3
import os
import email_password
import smtplib
import time
from tkinter import ttk
from sign_up import sign_up


class loginSystem:
    def __init__(self,dk):
        self.dk=dk
        self.dk.title("Login System")
        self.dk.geometry("1350x700+0+0")
        self.dk.config(bg="#fafafa")

        self.otp=''
        # ==================== all veraible =================
        self.var_emp_id=StringVar()
        self.var_password=StringVar()
        self.var_otp=StringVar()
        self.var_new_password=StringVar()
        self.var_confirm_password=StringVar()
# =========================== this is for time =================
        # self.lbl_clock=Label(self.dk,font=("ds_digital",25,),bg="black",fg="cyan",bd=6,relief=SUNKEN)
        # self.lbl_clock.place(x=700,y=30,width=200,height=50)
        
        # ================= images================
        self.phone_image=PhotoImage(file="images/phone.png")
        self.lbl_phone_image=Label(self.dk,image=self.phone_image,bd=0).place(x=200,y=70)

# =========================login frame ==============
        login_frame=Frame(self.dk,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=650,y=100,width=350,height=460)

        title=Label(login_frame,text="Login System",font=("goudy old style",30,"bold"),bg="white")
        title.place(x=0,y=30,relwidth=1)

        lbl_user=Label(login_frame,text="Employee ID",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=100)
        txt_user_name=Entry(login_frame,textvariable=self.var_emp_id,font=("times new roman",15),bg="#ECECEC").place(x=50,y=140,width=250)

        lbl_password=Label(login_frame,text="Password",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=200)
        txt_user_password=Entry(login_frame,textvariable=self.var_password,show="*",font=("times new roman",15),bg="#ECECEC").place(x=50,y=240,width=250)
        
        btn_login=Button(login_frame,text="Login",command=self.login,font=("Arial Rounded MT Bold",15),bg="green",cursor="hand2",activebackground="green",fg="white",activeforeground="white" ).place(x=50,y=300,width=250,height=36)

        lbl_hr=Label(login_frame,bg="lightgray").place(x=50,y=370,width=250,height=4)
        lbl_or=Label(login_frame,text="OR",font=("times new roman",15,"bold"),bg="white",fg="lightgray").place(x=150,y=355)

        btn_forgate=Button(login_frame,text="Forget Password?",command=self.forget_windo,font=("times new roman",15,"bold"),bg="white",fg="#00759E",cursor="hand2",bd=0,activebackground="white",activeforeground="#00759E").place(x=100,y=390)

# ======================= register frame ===========================
        register_frame=Frame(self.dk,bd=2,relief=RIDGE,bg="white")
        register_frame.place(x=650,y=570,width=350,height=60)

        lbl_or=Label(register_frame,text="Don't have an account?",font=("times new roman",15,"bold"),bg="white").place(x=30,y=12)
        btn_forgate=Button(register_frame,text="Sign Up",command=self.sign_up_win,font=("times new roman",15,"bold"),bg="white",fg="#00759E",cursor="hand2",bd=0,activebackground="white",activeforeground="#00759E").place(x=230,y=10)
# ================ animation images ============
        self.im1=PhotoImage(file="images\im1.png")
        self.im2=PhotoImage(file="images\im2.png")
        self.im3=PhotoImage(file="images\im3.png")

        self.lbl_change_image=Label(self.dk,bg="white")
        self.lbl_change_image.place(x=367,y=172,width=240,height=428)

        self.animate()
        # self.send_email('ava')
        # self.update_date_time()
# ========================== animation function =============
    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate)


# =================================== all function =======================================
    def login(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="" or self.var_password.get()=="":
                messagebox.showerror("Error","All fileds are required",parent=self.dk)

            else:
                cur.execute("select userType from employee where eid=? AND password=?",(self.var_emp_id.get(),self.var_password.get()))
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror("Error","Invalid user name/password",parent=self.dk)
                else:
                    if user[0]=="Admin":
                        self.dk.destroy()
                        os.system("python 01_dashboard.py")
                    else:
                        self.dk.destroy()
                        os.system("python billing.py")
                    

        except Exception as ex:
            messagebox.showerror("error",f"error due to : {str(ex)}",parent=self.dk)

    def forget_windo(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent=self.dk)
            else:
                cur.execute("select email from employee where eid=?",(self.var_emp_id.get(),))
                email=cur.fetchone()
                if email==None:
                    messagebox.showerror("Error","Invalid Employee ID,try again",parent=self.dk)
                else:
                    # ===== forget windo=====
                    # call_send_email_function()
                    chk=self.send_email(email[0])
                    if chk !='s':
                        messagebox.showerror("Error","Connection Error , try again",parent=self.dk)
                    else:
                        self.forget_win=Toplevel(self.dk)
                        self.forget_win.title('RESET PASSWORD')
                        self.forget_win.geometry('400x350+500+100')
                        self.forget_win.focus_force()

                        title=Label(self.forget_win,text="Reset Password",font=("goudy old style",15,"bold"),bg="#3f51b5",fg="white").pack(side=TOP,fill=X)

                        lbl_reset=Label(self.forget_win,text="Enter OTP sent on Registered Email",font=("Andalus",15)).place(x=20,y=60)
                        txt_reset=Entry(self.forget_win,textvariable=self.var_otp,font=("times new roman",15),bg="lightyellow").place(x=20,y=100,width=250,height=30)
            
                        lbl_new_pass=Label(self.forget_win,text="Enter New Password ",font=("Andalus",15)).place(x=20,y=160)
                        txt_new_pass=Entry(self.forget_win,textvariable=self.var_new_password,font=("times new roman",15),bg="lightyellow").place(x=20,y=190,width=250,height=30)

                        lbl_conf_pass=Label(self.forget_win,text="Enter Confirm Password",font=("Andalus",15)).place(x=20,y=225)
                        txt_conf_pass=Entry(self.forget_win,textvariable=self.var_confirm_password,font=("times new roman",15),bg="lightyellow").place(x=20,y=255,width=250,height=30)

                        self.btn_reset=Button(self.forget_win,text="SUBMIT",command=self.validate_otp,font=("times new roman",15,"bold"),bg="lightblue",fg="#00759E",cursor="hand2")
                        self.btn_reset.place(x=280,y=100,width=100,height=30)

                        self.btn_update=Button(self.forget_win,text="Update",command=self.update_password,state=DISABLED,font=("times new roman",15,"bold"),bg="lightblue",fg="#00759E",cursor="hand2")
                        self.btn_update.place(x=150,y=300,width=100,height=30)



                
        except Exception as ex:
            messagebox.showerror("error",f"error due to : {str(ex)}",parent=self.dk)

    def validate_otp(self):
        if int(self.otp)==int(self.var_otp.get()):
            self.btn_update.config(state=NORMAL)
            self.btn_reset.config(state=DISABLED)
        else:
            messagebox.showerror("Error","Invalid OTP, Try again",parent=self.forget_win)


    def update_password(self):
        if self.var_new_password.get()=="" or self.var_confirm_password.get()=="":
            messagebox.showerror("Error","Password is required",parent=self.forget_win)

        elif self.var_new_password.get()!=self.var_confirm_password.get():
            messagebox.showerror("Error","New Password & Confirm Password should be same",parent=self.forget_win)
        else:
            con=sqlite3.connect(database='ims.db')
            cur=con.cursor()
            try:
                cur.execute("Update employee SET password=? where eid=?",(self.var_new_password.get(),self.var_emp_id.get()))
                con.commit()
                messagebox.showinfo("Success","Password updated sucessfully",parent=self.forget_win)
                self.forget_win.destroy()
            except Exception as ex:
                messagebox.showerror("error",f"error due to : {str(ex)}",parent=self.dk)



    def send_email(self,to):
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        email_in=email_password.email_in
        pass_in=email_password.pass_in

        s.login(email_in, pass_in)

        self.otp=int(time.strftime("%H%S%M"))+int(time.strftime("%S"))
        # print(self.otp)
        subj='IMS-Reset Password OTP'
        msg=f'Dear Sir/Madam,\n\nYour Reset OTP is {str(self.otp)}.\n\nwith Regards,\nIMS Team'
        msg="Subject: {}\n\n{}".format(subj,msg)
        s.sendmail(email_in, to, msg)
        chk=s.ehlo()
        # chk=self.EHLO()
        if chk[0]==250:
            return 's'
        else:
            return 'f'

# ====================== time function =============
    # def update_date_time(self):
    #     time_in=time.strftime("%I.%M.%S %p")
    #     date_in=time.strftime("%d-%m-%Y")
    #     self.lbl_clock.config(text=f"{str(time_in)}")
    #     self.lbl_clock.after(200,self.update_date_time)


# ============================== sign up function ========================================

    def sign_up_win(self):
        self.new_win=Toplevel(self.dk)
        self.new_obj=sign_up(self.new_win)
    

      

dk=Tk()
obj=loginSystem(dk)
dk.mainloop()
