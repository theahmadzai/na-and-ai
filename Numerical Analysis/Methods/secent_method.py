from math import e
import tabulate as tb
import numpy as np
import matplotlib.pyplot as plt

# fx = lambda x: (x ** 3) - (3 * x) - 5
fx = lambda x: (4*(x**2)) + 5*x
sfx = lambda a, b: (a * fx(b) - b * fx(a)) / (fx(b) - fx(a))

X = np.linspace(-10, 10,1000)
Y = fx(X)

plt.plot(X,Y, color='orange')

a = -0.4
b = 0.3
ans = []

while round(fx(a), 4) != 0:
    ans.append([round(a, 4)])
    a, b = b, sfx(a, b)
    plt.plot([a, b], [fx(a), fx(b)], color='red')


print(tb.tabulate(ans, headers=['xn'], tablefmt='orgtbl', showindex='always'))
plt.show()
