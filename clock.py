from tkinter import *
#from tkinter.tkk import *

from time import strftime

root = Tk()
root.title("Clock")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("ds-digital", 80),background = "white", foreground = "black")
label.pack(anchor='center')
time()

mainloop()