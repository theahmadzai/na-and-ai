import pandas
from bokeh import plotting, io

data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
x=[]
y=[]

for i in range(-10,10,1):
    x.append(i)
    y.append((i**3)-(3*i)-6)

x1 = []
y1 = []
for i in range(-10,10,1):
    x1.append(i)
    y1.append((i**2)-(3*i)-6)

f = plotting.figure()

f.line(x,y,line_width=2)
f.circle(x, y, fill_color="white", size=8)

f.circle(x1,y1, fill_color="green", size=10)

io.output_file("bokeh_plot.html")
io.show(f)