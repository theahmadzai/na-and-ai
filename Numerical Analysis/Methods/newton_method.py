from math import e
import tabulate as tb
import numpy as np
import matplotlib.pyplot as plt

# fx = lambda x: (x ** 3) - (3 * x) - 5
# fdx = lambda x: ((x ** 3) - (3 * x) - 5) / (3 * (x ** 2) - 3)
# fix = lambda x: (x * ((x ** 3) - (6*x) - 20)) / 4

# fx = lambda x: e**(2*x) - 6
# fdx = lambda x: (e**(2*x) - 6) / (2*e**(2*x))

fx = lambda x: (-4*(x**2))+(3*x)
fdx = lambda x: fx(x) / ((-8*x)+3)

X = np.linspace(-10,10,1000)
Y = fx(X)

plt.plot(X,Y,color='orange')

x = (0.6+0.95)/2
ans = []

while round(fx(x), 8) != 0:
    ans.append([x, fx(x)])
    plt.plot([x,x],[0,fx(x)], marker='o', markersize=2, color="red")
    dx = x - fdx(x)
    plt.plot([x,dx], [fx(x), 0], marker='o', markersize=2, color="green")
    x = dx

print(tb.tabulate(ans, headers=['x', 'fx(x)'], tablefmt='orgtbl', showindex='always'))
plt.show()
