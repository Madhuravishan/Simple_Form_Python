from tkinter import*
from tkinter import ttk

def search():
    pass
        
    
def clear():
    entr1.delete(0,END)
    sp1box.delete(0,END)
    cb1.delete(0,END)
    cb2.delete(0,END)
win=Tk()
win.title("Form")
win.geometry("550x450")
win.configure(bg="#708090")
win.resizable(0,0)

title=["Mr","Miss","Mrs"]
course=["IIT","BIT","IT"]


lbl1=Label(win,text="Title",font="none 15",bg="#708090")
lbl1.place(x=20,y=100)
lbl2=Label(win,text="name:",font="none 15",bg="#708090")
lbl2.place(x=20,y=150)
lbl3=Label(win,text="Age",font="none 15",bg="#708090")
lbl3.place(x=20,y=200)
lbl4=Label(win,text="Course Name:",font="none 15",bg="#708090")
lbl4.place(x=20,y=250)
cb1=ttk.Combobox(win,font="none 15",width="10",values=title)
cb1.place(x=250,y=100)
entr1=Entry(win,font="none 15",width=25)
entr1.place(x=250,y=150)
sp1box=Spinbox(win,font="none 15",width="2",from_=19,to=60)
sp1box.place(x=250,y=200)
cb2=ttk.Combobox(win,font="none 15",width="10",values=course)
cb2.place(x=250,y=250)

btnsrh=Button(win,text="Add Data",font="none 15",width="15",bg="darkgray",command=search)
btnsrh.place(x=20,y=300)
win.bind("<Return>",lambda event:search())

btnclr=Button(win,text="clear",font="none 15",width="6",bg="darkgray",command=clear)
btnclr.place(x=250,y=300)
win.bind("<Escape>",lambda event:clear())




win.mainloop()

