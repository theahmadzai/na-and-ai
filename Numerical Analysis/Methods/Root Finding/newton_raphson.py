import tabulate as tb
import numpy as np
import matplotlib.pyplot as plt

fx = lambda x: (x ** 3) - (3 * x) - 5
fdx = lambda x: ((x ** 3) - (3 * x) - 5) / (3 * (x ** 2) - 3)

# plot function
X = np.linspace(-10, 10, 1000)
Y = fx(X)
plt.plot(X, Y, color='orange')

x = 9

ans = []

while round(fx(x), 8) != 0:
    # append result row to ans array
    ans.append([round(x, 4), round(fx(x), 4)])

    # plot x to f(x)
    plt.plot([x, x], [0, fx(x)], marker='o', markersize=2, color="red")
    plt.pause(0.2)
    dx = x - fdx(x)

    # plot the tangent line
    plt.plot([x, dx], [fx(x), 0], marker='o', markersize=2, color="green")
    plt.pause(0.2)
    x = dx

print(tb.tabulate(ans, headers=['x', 'y'], tablefmt='orgtbl', showindex='always'))
plt.show()
