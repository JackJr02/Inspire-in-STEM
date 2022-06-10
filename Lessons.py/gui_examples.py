#!/usr/bin/python
# Name:Jack Jr
# Date:31/05/2022
# GUI examples using Tkinker
######################

from tkinter import *

window = Tk()
window.title("Welcome to my app ")
window.configure(bg='blue')
window.geometry("700x600")

#Label Positioning
f_name=Label(window, text="Inspire-in-STEM ", font=("Arial Bold",14))
f_name.grid(column=30,row=100)


def open_popup():
    top=Toplevel(window)
    top.geometry("300x300")
    top.title("Pop Up Window")
    top.configure(bg='Black')
    msg=Label(top,text="Welcome to The Pop Up",font=('Mistral 18 bold')).place(x=150,y=150)

#Button Positioning
btn=Button(text="Click Here",bg='black',fg='white',command=open_popup().pa())
btn.grid(column=100,row=100)

#Box Positioning
f_name_box=Entry(window, width=10)
f_name_box.grid(column=110,row=120)


window.mainloop()
