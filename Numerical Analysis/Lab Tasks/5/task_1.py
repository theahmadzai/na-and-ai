import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Calculation')

ttk.Label(win, text='Number 1: ').grid(column=0, row = 0)
in1 = ttk.Entry(win)
in1.grid(column=1, row=0)

ttk.Label(win, text='Number 2: ').grid(column=0, row = 1)
in2 = ttk.Entry(win)
in2.grid(column=1, row=1)

def calculate(k):
    answer.delete(first=0,last=tk.END)
    answer.insert(0, eval(str(in1.get()) + str(k) + str(in2.get())))

ttk.Button(win, text='Sum', command=lambda : calculate('+')).grid(column=0, row=2)
ttk.Button(win, text='Sub', command=lambda : calculate('-')).grid(column=1, row=2)
ttk.Button(win, text='Mul', command=lambda : calculate('*')).grid(column=0, row=3)
ttk.Button(win, text='Div', command=lambda : calculate('/')).grid(column=1, row=3)

ttk.Label(win, text='Output of ').grid(column=0,row=4)
answer = ttk.Entry(win)
answer.grid(column=1,row=4)

win.mainloop()
