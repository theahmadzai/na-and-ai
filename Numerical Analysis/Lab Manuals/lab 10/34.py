# Question 34: Write python code for Secant Method code for equation (e**(2*x))-6

from math import e
import tabulate as tb
import numpy as np
import matplotlib.pyplot as plt

fx = lambda x: e**(2*x) - 6
sfx = lambda a, b: (a * fx(b) - b * fx(a)) / (fx(b) - fx(a))

# plot function
X = np.linspace(-10,10,1000)
Y = fx(X)
plt.plot(X,Y,color='orange')

a = -0.25
b = 9

ans = []

while round(fx(a), 4) != 0:
    ans.append([round(a, 4)])
    a, b = b, sfx(a, b)

    # plot secent lines
    plt.plot([a, b], [fx(a), fx(b)], color='red')

print(tb.tabulate(ans, headers=['xn'], tablefmt='orgtbl', showindex='always'))
plt.show()
