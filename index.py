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
        progress_label.after(100,load)
        progress_bar['value'] = 10*i
        i += 1

        if progress_bar['value']==100:
            main.destroy()

            admin()

load()
def admin():
    admin =Tk()

    height = 600
    width = 700
    x = (admin.winfo_screenwidth() // 2) - (width // 2)
    y = (admin.winfo_screenheight() // 2) - (height // 2)
    admin.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    #admin.overrideredirect(True)
    admin.config(background="#2f6c60")
    #login_frame = Frame(admin,width = 300,height = 400,bg = "white",relief = RAISED)
    #login_frame.place(relx = 0.28,rely = 0.2)

#====================================================selection page=====================================
    student_img = Button(admin,bg= 'white',relief = RAISED,bd =3)
    image_file = PhotoImage(file ='utility//std.png')
    student_img.config(image =image_file)
    student_img.place(relx = 0.2,rely =0.4)

    admin_img = Button(admin, bg='white', relief=RAISED, bd=3)
    admin_file = PhotoImage(file='utility//untitled-1.png')
    admin_img.config(image=admin_file)
    admin_img.place(relx=0.6, rely=0.4)



    admin.mainloop()



main.resizable(False,False)
main.mainloop()