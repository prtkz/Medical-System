from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random


def main():
    root=Tk()
    app = Window1(root)

class Window1:
    def __init__(self,master):
        self.master = master
        self.master.title("Sonali Medical")
        self.master.geometry('1350x750+0+0')
        self.master.config(background="lawngreen")
        self.frame = Frame(self.master)
        self.frame.pack()

        self.Username=StringVar()
        self.Password=StringVar()
##MainTitle##        
        self.LabelTitle=Label(self.frame,bg="yellow",fg="blue",text = 'Sonali Medical',font=('arial',50,'bold'),bd=20)
        self.LabelTitle.grid(row=0, column=0, columnspan=2, pady=40)
##LoginFrame##
        self.Loginframe1 = Frame(self.frame,width=1010,height=300,bd=20,relief='ridge')
        self.Loginframe1.grid(row=1, column= 0)

        self.Loginframe2 = Frame(self.frame,width=1010,height=100,bd=20,relief='ridge')
        self.Loginframe2.grid(row=2, column= 0)

        self.Loginframe3 = Frame(self.frame,width=1010,height=100,bd=20,relief='ridge')
        self.Loginframe3.grid(row=3, column= 0,pady=2)

##Username And Password##     
        self.lblUsername=Label(self.Loginframe1,text = 'Username',bg="limegreen",font=('arial',10,'bold'),bd=10)
        self.lblUsername.grid(row=0, column=0)

        self.txtUsername=Entry(self.Loginframe1,font=('arial',10,'bold'),bd=10,textvariable=self.Username)
        self.txtUsername.grid(row=0, column=1)

        
        self.lblPassword=Label(self.Loginframe1,text = 'Password',bg="limegreen",font=('arial',10,'bold'),bd=10)
        self.lblPassword.grid(row=1, column=0)

        self.txtPassword=Entry(self.Loginframe1,font=('arial',10,'bold'),bd=10,textvariable=self.Password)
        self.txtPassword.grid(row=1, column=1)

##Button##  
        self.btnLogin = Button(self.Loginframe2, text ="Login",width=17,bg="olivedrab",font=('arial',20,'bold'), command=self.Login_System)
        self.btnLogin.grid(row=0,column=0)

        self.btnExit = Button(self.Loginframe2,text ="Exit",width=17,bg="olivedrab",font=('arial',20,'bold'), command=self.Exit)
        self.btnExit.grid(row=0,column=1)


        self.btnRegistration = Button(self.Loginframe3, text ="Registration",bg="gold",state = DISABLED, command=self.Registration_window)
        self.btnRegistration.grid(row=0,column=0)

  
##Login Function##
    def Login_System(self):
            user = (self.Username.get())
            pswd = (self.Password.get())
            
            if (user == str('pratik')) and (pswd == str(12345)):
                self.btnRegistration.config(state= NORMAL)
               
            else:
                tkinter.messagebox.askokcancel("No user found")
                self.btnRegistration.config(state= DISABLED)
                
                self.Username.set("")
                self.Password.set("")
##Exit Function##
    def Exit(self):
            self.Exit = tkinter.messagebox.askyesno("Sonali Medical", 'Are you sure you want to Exit')
            if self.Exit>0:
               self.master.destroy()
            return
                
                

##Registration##
    def Registration_window(self):
        self.newWindow=Toplevel(self.master)
        self.app = Window2(self.newWindow)



##Customer Window##
class Window2:
    def __init__(self,root):
        self.root = root
        self.root.title("Registration")
        self.root.geometry('1350x750+0+0')
        self.frame = Frame(self.root)
        self.frame.pack()
        
 #################################################################################

        self.Firstname=StringVar()
        self.Lastname=StringVar()
        self.PhoneNo=IntVar()
        self.Medicine=StringVar()
        self.Quantity=StringVar()
        self.Price=StringVar()
        
       
##Frame##
        
        self.LabelTitle=Label(self.frame,text = 'Customer Registration',font=('arial',50,'bold'),bd=20)
        self.LabelTitle.grid(row=0, column=0, columnspan=2, pady=40)

        
##MainFrame##        
        self.CustomerName = Frame(self.frame,width=3010,height=800,bd=20,relief='ridge')
        self.CustomerName.grid(row=1, column= 0)

       
        self.lblFirstname=Label(self.CustomerName,text = 'First Name',font=('arial',10,'bold'),bd=10)
        self.lblFirstname.grid(row=0, column=0)

        self.txtFirstname=Entry(self.CustomerName,font=('arial',10,'bold'),bd=10,textvariable=self.Firstname)
        self.txtFirstname.grid(row=0, column=1)

        
        self.lblLastname=Label(self.CustomerName,text = 'Last Name',font=('arial',10,'bold'),bd=10)
        self.lblLastname.grid(row=1, column=0)

        self.txtLastname=Entry(self.CustomerName,font=('arial',10,'bold'),bd=10,textvariable=self.Lastname)
        self.txtLastname.grid(row=1, column=1)

        self.lblPhoneNo=Label(self.CustomerName,text = 'Mobile Number',font=('arial',10,'bold'),bd=10)
        self.lblPhoneNo.grid(row=2, column=0)

        self.txtPhoneNo=Entry(self.CustomerName,font=('arial',10,'bold'),bd=10,textvariable=self.PhoneNo)
        self.txtPhoneNo.grid(row=2, column=1)

       
        self.lblMedicine=Label(self.CustomerName,text = 'Medicine Name',font=('arial',10,'bold'),bd=10)
        self.lblMedicine.grid(row=3, column=0)

        self.txtMedicine=Entry(self.CustomerName,font=('arial',10,'bold'),bd=10,textvariable=self.Medicine)
        self.txtMedicine.grid(row=3, column=1)

        self.lblQty=Label(self.CustomerName,text = 'Quantity',font=('arial',10,'bold'),bd=10)
        self.lblQty.grid(row=4, column=0)

        self.txtQty=Entry(self.CustomerName,font=('arial',10,'bold'),bd=10,textvariable=self.Quantity)
        self.txtQty.grid(row=4, column=1)

        self.lblPrice=Label(self.CustomerName,text = 'Price Per Medicine',font=('arial',10,'bold'),bd=10)
        self.lblPrice.grid(row=5, column=0)

        self.txtPrice=Entry(self.CustomerName,font=('arial',10,'bold'),bd=10,textvariable=self.Price)
        self.txtPrice.grid(row=5, column=1)

        self.lblTotalAmt=Label(self.CustomerName,text = 'Total Amount',font=('arial',10,'bold'),bd=10)
        self.lblTotalAmt.grid(row=6, column=0)

        self.txtTotalAmt=Entry(self.CustomerName,font=('arial',10,'bold'),bd=10,textvariable=self.TotalAmt)
        self.txtTotalAmt.grid(row=6, column=1)

##Button##
        self.btnTotalAmt = Button(self.CustomerName,text ="Total",width=17,font=('arial',20,'bold'), command=self.TotalAmt)
        self.btnTotalAmt.grid(row=3,column=2)

        
        self.btnExit = Button(self.CustomerName,text ="Exit",width=17,font=('arial',20,'bold'), command=self.Exit)
        self.btnExit.grid(row=7,column=1)
   
        self.btnSubmit = Button(self.CustomerName, text ="Submit",width=17,font=('arial',20,'bold'), command=self.Submit)
        self.btnSubmit.grid(row=7,column=0)


##Function##

    def Details_System(self):
            Fname = (self.Firstname.get())
            Lname = (self.Lastname.get())
            MobNo = (self.PhoneNo.get())
            Medicine=(self.Medicine.get())            

     
    def Exit(self):
            self.Exit = tkinter.messagebox.askyesno("Sonali Medical", 'Are you sure you want to Exit')
            if self.Exit>0:
               self.root.destroy()
            return


           
    def TotalAmt(self):
        try:
            global exp
            totalvalue= str(eval(exp))
            equation.set(totalvalue)
            exp=((self.Quantity.get()) * (self.Price.get()))
        except:
            equation.set("error")



    def Submit(self):
            Fname = (self.Firstname.get())
            Lname = (self.Lastname.get())
            MobNo = (self.PhoneNo.get())
            Medicine=(self.Medicine.get())
            text_file=open("Customerdata.txt","w")
            text_file.write(Fname)
            text_file.write(Lname)
            
            text_file.close()


 ##################################################################################




if __name__== '__main__':
    main()
    
