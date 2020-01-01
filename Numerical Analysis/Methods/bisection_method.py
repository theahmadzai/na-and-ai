import tkinter as tk
from tkinter import ttk
from tabulate import *
import time
import pandas
from bokeh import plotting, io
import numpy as np

win = tk.Tk()
win.title('Bisection Method')
win.config(padx=20, pady=20)

inputsFrame = ttk.Frame(win)
inputsFrame.grid(row=0, column=0)

fmBox = ttk.Entry(inputsFrame)
fmBox.grid(row=0, column=0)
fmBox.insert(0,"(x ** 3) - (3 * x) - 5")
lower_limit = ttk.Entry(inputsFrame)
lower_limit.grid(row=0, column=1)
upper_limit = ttk.Entry(inputsFrame)
upper_limit.grid(row=0, column=2)

cols = ('n', 'a(-)', 'b(+)', 'mean', 'f(mean)')

answerBox = ttk.Treeview(win, columns=cols, show='headings')
answerBox.grid(row=1, column=0)

for col in cols:
    answerBox.heading(col, text=col)

def calculateBisection():
    fx = lambda x: eval(fmBox.get())

    a = float(lower_limit.get())
    b = float(upper_limit.get())

    f = plotting.figure()
    x = []
    y = []

    for i in np.arange(-5,5,0.01):
        x.append(i)
        y.append(fx(i))

    x1 = []
    y1 = []

    f.line(x, y, line_width=1)
    f.circle(x, y, fill_color="white", size=3)

    ans = []

    for i in range(16):
        x = (a + b) / 2
        x1.append(x)
        y1.append(fx(x))

        ans.append([i, round(a, 4), round(b, 4), round(x, 4), round(fx(x), 4)])
        answerBox.insert("", "end", values=(i, round(a, 4), round(b, 4), round(x, 4), round(fx(x), 4)))

        if fx(a) * fx(b) > 0:
            print('No solution exist.')
            break

        if fx(a) * fx(x) < 0:
            b = x
        else:
            a = x

    print(tabulate(ans, headers=['n', 'a(-)', 'b(+)', 'mean', 'f(mean)'], tablefmt='orgtbl'))
    f.circle(x1, y1, fill_color="green", size=5)
    io.output_file("bokeh_plot.html")
    io.show(f)

calculateButton = ttk.Button(inputsFrame, text='Calculate', command=calculateBisection)
calculateButton.grid(row=0, column=3)

win.mainloop()
