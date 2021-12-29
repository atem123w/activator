import os
from tkinter import *
window = Tk()  
window.title("активатор WINDOWS")  
  
  
def clicked():  
    os.system('slmgr.vbs/ipk 7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH')
    os.system('slmgr.vbs/skms kms8.msguides.com')
    os.system('slmgr.vbs/ato')
def clicked1():  
    os.startfile('active_CoreSingleLang_Home.bat','runas')
  
lbl = Label(window, text="Выберите свою редакцию WINDOWS11 ", font=("Arial Bold", 10))  
lbl.grid(column=0, row=0)  
btn = Button(text="активировать win11 HOME CoreSingleLanguage ", command=clicked)  
btn.grid(column=0, row=1)
btn = Button(text="                       активировать win11 PRO                   ", command=clicked1)  
btn.grid(column=0, row=2)
window.mainloop()