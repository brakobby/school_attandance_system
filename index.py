from tkinter import *
import time
from tkinter import ttk
from tkinter.ttk import Progressbar
import os
import sys
#=================================================setting up window=====================================================

main = Tk()
#image = PhotoImage(file =" asserts//background.png")
height = 430
width = 530
x= (main.winfo_screenwidth()//2)-(width//2)
y = (main.winfo_screenheight()//2)-(height//2)
main.geometry('{}x{}+{}+{}'.format(width,height,x,y))
main.overrideredirect(True)
main.config(background = "#2f6c60")

#=================================================window content=====================================================
welcome_label = Label(main,text = "Welcome To Vartsy Computer School",bg="#2f6c60",font = ('arial',18,'bold'),fg ="#ffffff")
welcome_label.place(relx = 0.1,rely =0.1)

progress_label = Label(main,text = "Please Wait...",bg="#2f6c60",font = ('arial',14,'bold'),fg ="#ffffff")
progress_label.place(relx = 0.4,rely = 0.75)
progress_bar = Progressbar(main,length = 500,orient =HORIZONTAL,mode = 'determinate')
progress_bar.place(relx = 0.02,rely =0.88)
#=================================================window exit=====================================================
def exit_window():
    sys.exit(main.destroy())

#=================================================progressbar function=====================================================
i=0
def load():
    global i
    if i <=10:
        txt="Please wait..."+(str(10*i)+'%')
        progress_label.config(text=txt)
        progress_label.after(1000,load)
        progress_bar['value'] = 10*i
        i += 1

        if progress_bar['value']==100:
            main.destroy()

            admin()

def admin():
    admin =Tk()

    height = 780
    width = 870
    x = (admin.winfo_screenwidth() // 2) - (width // 2)
    y = (admin.winfo_screenheight() // 2) - (height // 2)
    admin.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    #admin.overrideredirect(True)
    admin.config(background="#2f6c60")
    admin.mainloop()






load()

main.resizable(False,False)
main.mainloop()