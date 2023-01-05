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
main.config(background = "black")

#=================================================window content=====================================================
welcome_label = Label(main,text = "Welcome To Vartsy Computer School",bg="black",font = ('arial',18,'bold'),fg ="#ffffff")
welcome_label.place(relx = 0.1,rely =0.1)

progress_label = Label(main,text = "loading Program files...",bg="black",font = ('arial',14,'bold'),fg ="#ffffff")
progress_label.place(relx = 0.35,rely = 0.75)
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
    nave_frame = Frame(admin,width = width,height = 70,bg = 'black')
    nave_frame.place(relx = 0,rely = 0)
    content = Frame(admin,width = width,height = height,bg = 'white')
    content.place(relx = 0,rely = 0.1)
    nav_label = Label(nave_frame,text = "VARTSY",font = ('arial',15,"bold"),fg = "white",bg ="black")
    nav_label.place(relx = 0.02,rely = 0.2)
    help_btn = Button(nave_frame, text="?", font=('arial', 17, "bold"), fg="red", bg="black",bd =0)
    help_btn.place(relx=0.9, rely=0.2)


#====================================================selection page=====================================
    def student():
        std_content = Frame(admin, width=width, height=height, bg='white')
        std_content.place(relx=0, rely=0.1)
        side_nav = Frame(std_content,width=230, height=height, bg='white',bd = 2,relief =RAISED)
        side_nav.place(relx = 0,rely =0.01)
        sign = Label(side_nav,text = '@brakobby',font = ('arial',12),bg ="white",fg ="red")
        sign.place(relx = 0.3,rely = 0.82)
        """avatar_label_image = Label(side_nav,bg ="black")
        avatar_image = PhotoImage(file ="utility//logo.png")
        avatar_label_image.config(image = avatar_image)
        avatar_label_image.place(relx = 0.02,rely = 0.05)"""
    #======================================regidtratiion and passport frame================================================
        reg_frame = Frame(std_content,width = width-230,height = height,bg ="navajowhite")
        reg_frame.place(relx=0.33,rely = 0)
        passport_frame = Frame(reg_frame,width=140,height = 160,bd = 2,relief = SUNKEN)
        passport_frame.place(relx =0.33,rely = 0.05)
        passprt_btn = Button(reg_frame,text = "Upload Passport-size photo",bd = 0,bg= "navajowhite",fg = 'red',font = ('arial',10,'bold'))
        passprt_btn.place(relx = 0.28,rely = 0.35)
    #==================================labels and Entries==================================================
        student_id = Label(reg_frame,text = 'Student Id',bg = "navajowhite",fg = "black",)

    student_img = Button(content,bg= 'white',relief = RAISED,bd =0)
    image_file = PhotoImage(file ='utility//untitled-1.png')
    student_img.config(image =image_file)
    student_img.place(relx = 0.2,rely =0.28)
    btn_lbl_1 =Label(content,text = 'Student',font = ('arial',18),bg ="white",fg ="black",bd =0)
    btn_lbl_1.place(relx =0.23,rely =0.6 )
    student_img.config(command = student)

    admin_img = Button(content, bg='white', relief=RAISED, bd=0)
    admin_file = PhotoImage(file='utility//untitled-1.png')
    admin_img.config(image=admin_file)
    admin_img.place(relx=0.6, rely=0.28)
    btn_lbl_2 = Label(content, text='Admin', font=('arial', 18), bg="white", fg="black", bd=0)
    btn_lbl_2.place(relx=0.63, rely=0.6)
    admin_img.config(command = administrator)


    admin.resizable(False,False)
    admin.mainloop()


def administrator():
    pass

def exit():
    pass

main.resizable(False,False)
main.mainloop()