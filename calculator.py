from tkinter import *
window=Tk()
window.title("project1")
window.geometry("500x500")
window.configure(bg="black")
label1=Label(window,text="CALCULATOR",fg="black",bg="white",font=("Arial",30))
label1.place(x=110,y=10)
label2=Label(window,text="Num :1",fg="black",bg="white",font=("Arial",20))
label2.place(x=110,y=80)
label3=Label(window,text="Num :2",fg="black",bg="white",font=("Arial",20))
label3.place(x=110,y=160)
label4=Label(window,text="Answer",fg="black",bg="white",font=("Arial",20))
label4.place(x=110,y=240)
def Add():
    plus=num1.get()+num2.get()
    entry3.delete(0,(END))
    entry3.insert(0,str(plus))
def Sub():
    minus=num1.get()-num2.get()
    entry3.delete(0,(END))
    entry3.insert(0,str(minus))
def Mult():
    pro=num1.get()*num2.get()
    entry3.delete(0,(END))
    entry3.insert(0,str(pro))
def Div():
    div=num1.get()/num2.get()
    entry3.delete(0,(END))
    entry3.insert(0,str(div))
num1=IntVar()
num2=IntVar()
num3=IntVar()
entry1=Entry(window,fg="black",bg="white",font=("Arial",20),textvariable=num1)
entry1.place(x=280,y=80,height=38,width=100)
entry2=Entry(window,fg="black",bg="white",font=("Arial",20),textvariable=num2)
entry2.place(x=280,y=160,height=38,width=100)
entry3=Entry(window,fg="black",bg="white",font=("Arial",20),textvariable=num3)
entry3.place(x=280,y=240,height=38,width=100)
button1=Button(window,text="+",fg="black",bg="white",font=("Arial",20),command=Add)
button1.place(x=100,y=400)
button2=Button(window,text="-",fg="black",bg="white",font=("Arial",20),command=Sub)
button2.place(x=200,y=400)
button3=Button(window,text="*",fg="black",bg="white",font=("Arial",20),command=Mult)
button3.place(x=300,y=400)
button4=Button(window,text="/",fg="black",bg="white",font=("Arial",20),command=Div)
button4.place(x=400,y=400)




    
window.mainloop()