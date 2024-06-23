from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Task 3")
root.geometry("700x1000")
root.configure(bg="#00563B")
label=Label(root,text="Contact Book",font=('Arial',50),fg="black",bg="#B2AC88")
label.pack()
label1=Label(root,text="Name",font=('Arial',30),fg="black",bg="#B2AC88")
label1.place(x=10,y=100,height=70,width=300)
label1=Label(root,text="Phone num",font=('Arial',30),fg="black",bg="#B2AC88")
label1.place(x=10,y=200,height=70,width=300)
name=StringVar()
num=IntVar()
entry=Entry(root,font=('Arial',30),fg="black",bg="#B2AC88",textvariable=name)
entry.place(x=400,y=100,height=70,width=300)
entry1=Entry(root,font=('Arial',30),fg="black",bg="#B2AC88",textvariable=num)
entry1.place(x=400,y=200,height=70,width=300)
def Add():
    nam=name.get()
    num1=num.get()
    if nam and num1:
        contact_list.insert(END,f"{nam}:{num1}")
        nam.delete(0,END)
        num1.delete(0,END)
    else:
        messagebox.showwarning("Warning  please enter both name and phone number")
def Del():
    select=contact_list.curselection()
    if select:
        contact_list.delete(select)
button=Button(root,text="Add Details",font=('Arial',30),fg="black",bg="#B2AC88",command=Add)
button.place(x=10,y=300)
button1=Button(root,text="Delete Details",font=('Arial',30),fg="black",bg="#B2AC88",command=Del)
button1.place(x=300,y=300)
contact_list=Listbox(root,font=('Arial',30),fg="black",bg="#B2AC88")
contact_list.place(x=100,y=400)
root.mainloop()