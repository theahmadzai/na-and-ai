from math import *
from tabulate import *
from bokeh import plotting, io
import numpy as np

ff = lambda x: (x ** 3) - (3 * x) - 5
fx = lambda a, b: ((a * ((e ** (2 * b)) - 6)) - (b * ((e ** (2 * a)) - 6))) / ((e ** (2 * b)) - (e ** (2 * a)))

a = 0.5
b = 1

px = []
py = []
for i in np.arange(-10,10,0.01):
    px.append(i)
    py.append(ff(i))

fig = plotting.figure()
fig.line(px,py,line_width=2)

ans = []

px1 = []
py1 = []

for i in range(7):
    ans.append([i, round(a, 4)])
    a, b = b, fx(a, b)
    px1.append(a)
    py1.append(b)

fig.circle(px1,py1, line_width=2, fill_color='green')
print(tabulate(ans, headers=['n', 'xn'], tablefmt='orgtbl'))
io.output_file('bokeh_plot.html')
io.show(fig)