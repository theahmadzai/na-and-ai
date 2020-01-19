import tkinter as tk
from tkinter import ttk
from math import e
import tabulate as tb
import numpy as np
import matplotlib.pyplot as plt

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

    X = np.linspace(-5, 5, 1000)
    Y = fx(X)

    plt.plot(X, Y, color='orange')

    ans = []

    x = (a + b) / 2

    while round(fx(x), 4) != 0:
        x = (a + b) / 2
        plt.plot(x, fx(x), marker='o', markersize=3, color='red')
        ans.append([round(a, 4), round(b, 4), round(x, 4), round(fx(x), 4)])
        answerBox.insert("", "end", values=(round(a, 4), round(b, 4), round(x, 4), round(fx(x), 4)))

        if fx(a) * fx(b) > 0:
            print('No solution exist.')
            break

        if fx(a) * fx(x) < 0:
            b = x
        else:
            a = x

    print(tb.tabulate(ans, headers=['a(-)', 'b(+)', 'mean', 'f(mean)'], tablefmt='orgtbl', showindex='always'))
    plt.show()


calculateButton = ttk.Button(inputsFrame, text='Calculate', command=calculateBisection)
calculateButton.grid(row=0, column=3)

win.mainloop()
