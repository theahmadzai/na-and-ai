# Question 33: Write python code for Newton Method code for equation (e**(2*x))-6

from math import e
import tabulate as tb
import numpy as np
import matplotlib.pyplot as plt

fx = lambda x: e**(2*x) - 6
fdx = lambda x: fx(x) / (2*e**(2*x))

# plot function
X = np.linspace(-10,10,1000)
Y = fx(X)
plt.plot(X,Y,color='orange')

x = 9.6

ans = []

while round(fx(x), 8) != 0:
    # append result row
    ans.append([x, fx(x)])

    # plot tangent lines
    plt.plot([x,x],[0,fx(x)], marker='o', markersize=2, color="red")
    dx = x - fdx(x)
    plt.plot([x,dx], [fx(x), 0], marker='o', markersize=2, color="green")
    x = dx

print(tb.tabulate(ans, headers=['x', 'fx(x)'], tablefmt='orgtbl', showindex='always'))
plt.show()
