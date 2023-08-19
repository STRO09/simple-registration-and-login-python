from tkinter import *
from tkinter import messagebox
import ast
import mysql.connector
import re
#SETTING UP
window=Tk()
window.title("REGISTRATION")
window.geometry('925x500+300+200')
window.configure(bg='#fff')
window.resizable(False,False)

#PHOTO
img=PhotoImage(file='signin.png')
Label(window,image=img,bg='white').place(x=50,y=50)

#icon image
imgg=PhotoImage(file="actionkamen.png")
window.iconphoto(False,imgg)

#FRAME FOR BUTTONS
frame=Frame(window,width=350,height=350,bg='white').place(x=480,y=50)#AliceBlue
heading=Label(frame,text='CREATE YOUR ACCOUNT',fg='#57a1f8',bg='white',font=('MIcrosoft YaHei UI Light',19,'bold')).place(x=500,y=50)


#FUNCTIONS FOR INPUTS
def on_enter(e):
    name=user.get()
    if name=="" or name=="Username":
        user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=="" :
        user.insert(0,'Username')

def on_enter1(e):
    passwo=passw.get()
    if passwo=="" or passwo=="Password":
        passw.delete(0,'end')
    
def on_leave1(e):
    passwo=passw.get()
    if passwo=="" :
        passw.insert(0,'Password')

def on_enter2(e):
    passwo=passw2.get()
    if passwo=="" or passwo=="Confirm Your Password":
        passw2.delete(0,'end')
    passw2.config(show="*")

def on_leave2(e):
    passwo=passw2.get()
    if passwo=="" :
        passw2.insert(0,'Confirm Your Password')

def on_enter3(e):
    em=email.get()
    if em=="" or em=="Email ID":
        email.delete(0,'end')

def on_leave3(e):
    em=email.get()
    if em=="" :
        email.insert(0,'Email ID')

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
def isValid(email):
    if re.fullmatch(regex, email):
        return True
    else:
        return False

def signin():
    username=user.get()
    em=email.get()
    password=passw.get()
    cpassword=passw2.get()
    
    if username=="" or em=="" or passw=="" or cpassword==""or username=="Username" or em=="Email ID" or passw=="Password" or cpassword=="Confirm Your Password":
        messagebox.showerror("Sign up failed","PLEASE FILL IN ALL CREDENTIALS")

    elif cpassword!=password:
            messagebox.showerror("BOTH PASSWORDS SHOULD MATCH")
    
    elif isValid(em)==False:
        messagebox.showerror("Sign up failed","EMAIL FORMAT WRONG")

        

    else:

        try:
            mydb = mysql.connector.connect(host="localhost",user="root",password="tfws.wow///POP()")
            mycursor = mydb.cursor()
        except:
            messagebox.showerror('Error', 'Database connectivity issues')
            return
        try:
            query = "create database userdata;"
            mycursor.execute(query)
            query = "use userdata;"
            mycursor.execute(query)
            query = "create table register(srno int auto_increment primary key not null,username varchar(100), email varchar(50),password varchar(20));"
            mycursor.execute(query)

        except:
            mycursor.execute('use userdata')
        
        query = 'select * from register where username=%s and password=%s'
        mycursor.execute(query,(user.get(), passw.get()))
        row = mycursor.fetchone()
        if row != None:
            messagebox.showerror('Error', 'USERNAME OR PASSWORD ALREADY TAKEN')
        else:
            query = 'insert into register(username,email,password)values(%s,%s,%s)'
            mycursor.execute(query,(user.get(),email.get(),passw.get()))
            mydb.commit()
            mydb.close()
            messagebox.showinfo('Success', 'Registration is successful')
            window.destroy()
            import loginpage
              
def loginpage():
    window.destroy()
    import loginpage

#hide and show button
button_mode=True

def hide():
    global button_mode
    if button_mode:
        eyeButton.config(image=openeye,activebackground="white")
        passw3=passw.get()
        if passw3=="Password":
            passw.delete(0,'end')
        passw.config(show="*")
        button_mode=False
    else:
        eyeButton.config(image=closeeye,activebackground="white")
        passw3=passw.get()
        if passw3=="":
            passw.insert(0,'Password')
        passw.config(show="")
        button_mode=True


openey=PhotoImage(file="seen.png")
openeye=openey.subsample(30,30)
closeey=PhotoImage(file="hide.png")
closeeye=closeey.subsample(30,30)
eyeButton=Button(frame,image=closeeye,bg="white",fg='White',cursor="hand2",border=0,command=hide)
eyeButton.place(x=740,y=190)

#INPUTS
user=Entry(frame,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",10))
user.place(x=560,y=110)
user.insert(0,"Username")
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)
#LINES UNDER INPUT(SHAPE)
Frame(frame,width=200,height=2,bg='black').place(x=560,y=135)

passw=Entry(frame,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",10))
passw.place(x=560,y=190)
passw.insert(0,"Password")
passw.bind('<FocusIn>',on_enter1)
passw.bind('<FocusOut>',on_leave1)
Frame(frame,width=200,height=2,bg='black').place(x=560,y=215)

passw2=Entry(frame,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",10))
passw2.place(x=560,y=230)
passw2.insert(0,"Confirm Your Password")
passw2.bind('<FocusIn>',on_enter2)
passw2.bind('<FocusOut>',on_leave2)
Frame(frame,width=200,height=2,bg='black').place(x=560,y=255)


email=Entry(frame,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",10))
email.place(x=560,y=150)
email.insert(0,"Email ID")
email.bind('<FocusIn>',on_enter3)
email.bind('<FocusOut>',on_leave3)
Frame(frame,width=200,height=2,bg='black').place(x=560,y=175)


#BUTTONS
Button(frame,width=39,pady=9,text='Sign In',cursor='hand2',bg='#57a1f8',fg='White',border=0,command=signin).place(x=520,y=290)

label=Label(frame,text="Already Have an Account?",fg='black',bg='white',font=("Microsoft YaHei UI Light",10)).place(x=543,y=350)
Button(frame,width=4,text='Log In',cursor='hand2',fg='#57a1f8',bg='White',border=0,command=loginpage).place(x=707,y=352)

#FRAME BOUNDARIES
'''Frame(frame,width=350,height=2,bg='black').place(x=480,y=50)
Frame(frame,width=2,height=350,bg='black').place(x=480,y=50)
Frame(frame,width=350,height=2,bg='black').place(x=480,y=400)
Frame(frame,width=2,height=350,bg='black').place(x=830,y=50)'''

window.mainloop()
