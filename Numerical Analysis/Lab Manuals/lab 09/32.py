# Question 32: Write python code for Bisection Method code for equation (e**(2*x))-6

from math import e
import tabulate as tb
import numpy as np
import matplotlib.pyplot as plt

fx = lambda x: (e**(2*x))-6
mean = lambda a,b: (a+b)/2

a = -5
b = 5

# Plot function
X = np.linspace(-5, 5, 1000)
Y = fx(X)
plt.plot(X, Y, color='orange')

ans = []

while round(fx(mean(a,b)), 4) != 0:
    x = mean(a,b)

    # append result row to ans array
    ans.append([round(a, 4), round(b, 4), round(x, 4), round(fx(x), 4)])

    # plot mid points
    plt.plot(x, fx(x), marker='o', markersize=3, color='red')

    if fx(a) * fx(b) > 0:
        print('No solution exist.')
        break

    if fx(a) * fx(x) < 0:
        b = x
    else:
        a = x

print(tb.tabulate(ans, headers=['a(-)', 'b(+)', 'mean', 'f(mean)'], tablefmt='orgtbl', showindex='always'))
plt.show()