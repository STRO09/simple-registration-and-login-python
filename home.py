from tkinter import *

homep=Tk()

homep.title("HOMEPAGE")
homep.geometry('925x500+300+200')
homep.configure(bg='#fff')
homep.resizable(False,False)

frame=Frame(homep,width=350,height=350,bg='white').place(x=0,y=0)#AliceBlue
heading=Label(frame,text='HELLO !!!',fg='#57a1f8',bg='white',font=('MIcrosoft YaHei UI Light',25,'bold')).place(x=50,y=50)


label=Label(frame,text="THIS IS HOW YOU CAN",fg='black',bg='white',font=("Microsoft YaHei UI Light",40)).place(x=50,y=100)
label=Label(frame,text="IMPLEMENT SIMPLE REGISTRATION AND LOGIN SYSTEM",fg='black',bg='white',font=("Microsoft YaHei UI Light",40)).place(x=50,y=200)
label=Label(frame,text="AND LOGIN SYSTEM",fg='black',bg='white',font=("Microsoft YaHei UI Light",40)).place(x=50,y=300)
homep.mainloop()