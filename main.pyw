import os
from tkinter import *
window = Tk()  
window.title("активатор WINDOWS")  
  
  
def clicked():  
    os.startfile('active_CoreSingleLang_Home.bat','runas')
def clicked1():  
    os.startfile('active_PRO.bat','runas')
  
lbl = Label(window, text="Выберите свою редакцию WINDOWS11\10 ", font=("Arial Bold", 10))  
lbl.grid(column=0, row=0)  
btn = Button(text="активировать win11/10 HOME  ", command=clicked)  
btn.grid(column=0, row=1)
btn = Button(text="                       активировать win11/10 PRO                   ", command=clicked1)  
btn.grid(column=0, row=2)
window.mainloop()
