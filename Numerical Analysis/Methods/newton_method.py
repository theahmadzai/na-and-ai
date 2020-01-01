from math import *
from tabulate import *
from bokeh import plotting, io
import numpy as np

f = plotting.figure()

fx = lambda x: (x ** 3) - (3 * x) - 5

px = []
py = []

for i in np.arange(-5, 5, 0.01):
    px.append(i)
    py.append(fx(i))

x = (0.5 + 1) / 2

ans = []

px1 = []
py1 = []
for i in range(5):
    ans.append([i, round(x, 4)])
    px1.append(x)
    py1.append(fx(x))
    x = fx(x)

f.line(px,py,line_width=2)
f.circle(px1, py1,fill_color="green", size=5)
io.output_file('bokeh_plot.html')
io.show(f)
print(tabulate(ans, headers=['n', 'xn'], tablefmt='orgtbl'))
