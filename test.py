from tkinter import *
from tkinter import messagebox
win = Tk()
win.title("Temprature calculator")
def convert(args):
    a=f.get()
    at=0
    at=int(a)
    ad=((at)-32)*(5/9)
    c.insert(0,str(ad))


Label(win, text='Forenheit').grid(row=0)
Label(win, text='Celsius').grid(row=1)
f = Entry(win)
c = Entry(win)
f.grid(row=0, column=1)
c.grid(row=1, column=1)

fr = Label(win, text='...')
fr.grid(row=0, column=3)
cr = Label(win, text='...')
cr.grid(row=1, column=3)




Button(win, text='Convert', command=convert).grid(row=2)

win.mainloop()
