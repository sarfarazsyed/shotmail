from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from s_e import *
c = 0
def mailit():
    mid = user.get()
    sub1 = sub.get()
    mes1 = mes.get()
    det1 = det.get()
    m ='Thanks for using our sevice \n\n' + mailto(mid,pwd.get(),sub1,mes1,det1)
    messagebox.showinfo("SSA Mail Client", m)

def browsefunc():
    global c
    if(c==0):
        f_name = filedialog.askopenfilename(filetypes = (("text files","*.txt"),("all files","*.*")))
        mes.insert(0,f_name)
    else:
        f_name = filedialog.askopenfilename(filetypes = (("XLSX files","*.xlsx"),("all files","*.*")))
        det.insert(0,f_name)
    c+=1
    
window = Tk()
window.configure(background="#900C3F")
window.geometry("500x650")
window.title("Shot Mail")

lab = Label(window,text="\nPlease Fill Details to send",fg="#FFFCF9",bg="#900C3F",font = ("Helvetica" , 16,"bold"))
lab.pack()

lab_u = Label(window,text = "\nEnter Gmail :",fg="#FFFCF9",bg="#900C3F",font = ("Times" , 12,"bold"))
user=Entry(window,width=35)
lab_u.pack()
user.pack()

lab_p = Label(window,text="\nEnter password : ",fg="#FFFCF9",bg="#900C3F",font = ("Times" , 12,"bold"))
pwd=Entry(window,show="*",width=35)
lab_p.pack()
pwd.pack()


lab_u = Label(window,text = "\nEnter Subject :" ,fg="#FFFCF9",bg="#900C3F",font = ("Times" , 12,"bold"))
sub=Entry(window,width=35)
lab_u.pack()
sub.pack()

lab_m = Label(window,text = "\nSelect Message File :",fg="#FFFCF9",bg="#900C3F",font = ("Times" , 12,"bold"))
lab_m.pack()
mes = Entry(window,width=50)
mes.pack()
lab_space = Label(window,bg="#900C3F")
lab_space.pack()
browsebutton = Button(window, text="Browse",fg="#900C3F",bg="#FFFCF9", command=browsefunc)
browsebutton.pack()


lab_d = Label(window,text = "\nSelect Details File :",fg="#FFFCF9",bg="#900C3F",font = ("Times" , 12,"bold"))
lab_d.pack()
det = Entry(window,width=50)
det.pack()
lab_space = Label(window,bg="#900C3F")
lab_space.pack()
browsebutton = Button(window, text="Browse",fg="#900C3F",bg="#FFFCF9", command=browsefunc)
browsebutton.pack()


lab_space = Label(window,bg="#900C3F")
lab_space.pack()




btn = Button(window,text="SEND",fg="#900C3F",bg="#FFFCF9",font = ("Times" , 13,"bold"), command = mailit)
btn.pack()


lab_c = Label(window,text="\n**MAKE SURE DETAILS FILE IS IN .xlsx FORMAT AND DATA IN Sheet1**\n**MAKE SURE YOU HAVE ENTERED CORRECT DETAILS**\n",fg="#FFFCF9",bg="#900C3F",font = ("Helvetica" , 10,"bold"))
lab_c.pack()


window.mainloop()
