from tkinter import *
from tkinter import messagebox
import mysql.connector
#SETTING UP
root=Tk()
root.title("LOGIN")
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)

#PHOTO
img=PhotoImage(file='login.png')
Label(root,image=img,bg='white').place(x=50,y=50)

#FRAME FOR BUTTONS
frame=Frame(root,width=350,height=350,bg='white').place(x=480,y=50)#AliceBlue
heading=Label(frame,text='LOG IN',fg='#57a1f8',bg='white',font=('MIcrosoft YaHei UI Light',23,'bold')).place(x=600,y=50)


#FUNCTIONS FOR INPUTS
def on_enter(e):
    name=user.get()
    if name=="" or name=="Username or Email":
        user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=="" :
        user.insert(0,'Username or Email')

def on_enter1(e):
    passwo=passw.get()
    if passwo=="" or passwo=="Password":
        passw.delete(0,'end')

def on_leave1(e):
    passwo=passw.get()
    if passwo=="" :
        passw.insert(0,'Password')

def signinpage():
    root.destroy()
    import Signin

def login1():
    username=user.get()
    password=passw.get()
    if username=='' or password=='' or username=="Username or Email" or password=="Password":
        messagebox.showerror('Error','All Field are required')
    else:
        try:
            mydb = mysql.connector.connect(host="localhost",user="root",password="tfws.wow///POP()")
            mycursor=mydb.cursor()
        except:
            messagebox.showerror('Error','Connection not established try again')
            return
        query = "use userdata;"
        mycursor.execute(query)
        query = 'select * from register where username=%s or email=%s or password=%s'
        mycursor.execute(query,(user.get(),user.get(),passw.get()))
        row = mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Invalid name and password')
        else:
            messagebox.showinfo('Welcome','Login is sucessful')
            root.destroy()
            import home

#hide and show button
button_mode=True

def hide():
    global button_mode
    if button_mode:
        eyeButton.config(image=openeye,activebackground="white")
        passw3=passw.get()
        if passw3=="Password":
            passw.delete(0,'end')
        else:
            passw.config(show="*")
        button_mode=False
    else:
        eyeButton.config(image=closeeye,activebackground="white")
        passw3=passw.get()
        if passw3=="":
            passw.insert(0,'Password')
        else:
            passw.config(show="")
        button_mode=True


openey=PhotoImage(file="seen.png")
openeye=openey.subsample(30,30)
closeey=PhotoImage(file="hide.png")
closeeye=closeey.subsample(30,30)
eyeButton=Button(frame,image=closeeye,bg="white",fg='White',cursor="hand2",border=0,command=hide)
eyeButton.place(x=740,y=180)

#INPUTS
user=Entry(frame,width=20,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",11))
user.place(x=560,y=120)
user.insert(0,"Username or Email")
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)
#LINES UNDER INPUT(SHAPE)
Frame(frame,width=200,height=2,bg='black').place(x=560,y=145)

passw=Entry(frame,width=20,fg='black',border=0,font=("Microsoft YaHei UI Light",11))
passw.place(x=560,y=180)
passw.insert(0,"Password")
passw.bind('<FocusIn>',on_enter1)
passw.bind('<FocusOut>',on_leave1)

Frame(frame,width=200,height=2,bg='black').place(x=560,y=205)

#BUTTONS
Button(frame,width=39,pady=9,text='Log In',cursor='hand2',bg='#57a1f8',fg='White',border=0,command=login1).place(x=520,y=270)

label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=("Microsoft YaHei UI Light",10)).place(x=550,y=330)
Button(frame,width=8,text='Sign up',cursor='hand2',fg='#57a1f8',bg='White',border=0,command=signinpage).place(x=695,y=332)

#FRAME BOUNDARIES
'''Frame(frame,width=350,height=2,bg='black').place(x=480,y=50)
Frame(frame,width=2,height=350,bg='black').place(x=480,y=50)
Frame(frame,width=350,height=2,bg='black').place(x=480,y=400)
Frame(frame,width=2,height=350,bg='black').place(x=830,y=50)'''

root.mainloop()
