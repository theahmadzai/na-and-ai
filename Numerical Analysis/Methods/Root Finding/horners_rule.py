import tabulate as tb
import numpy as np
import matplotlib.pyplot as plt

fx = lambda x: x ** 2 - x - 12

# plot function
X = np.linspace(-10, 10, 1000)
Y = fx(X)
plt.plot(X, Y, color='orange')


def div(p, x):
    r = []
    j = 0

    for n in p:
        r.append(n + j)
        j = r[-1] * x

    return r


p = [1, -1, -12]
x = 9

ans = []

while fx(x) != 0:
    # append result row to ans array
    ans.append([round(x, 4), round(fx(x), 4)])

    # plot x to fx(x) line
    plt.plot([x, x], [0, fx(x)], color='red')
    plt.pause(0.2)

    a = div(p, x)
    b = div(a[:-1], x)
    x -= a[-1] / b[-1]

print(tb.tabulate(ans, headers=['x', 'y'], tablefmt='orgtbl', showindex='always'))
plt.show()
