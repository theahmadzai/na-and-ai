import tabulate as tb
import numpy as np
import matplotlib.pyplot as plt

fx = lambda x: (x ** 3) - (3 * x) - 5
mean = lambda a, b: (a + b) / 2

# plot function
X = np.linspace(-5, 5, 1000)
Y = fx(X)
plt.plot(X, Y, color='orange')

a = -5
b = 5

ans = []

while round(fx(a), 4) != 0:
    x = mean(a, b)

    # append result row to ans array
    ans.append([round(a, 4), round(b, 4), round(x, 4), round(fx(x), 4)])

    # plot mid point
    plt.plot(x, fx(x), marker='o', markersize=3, color='red')
    plt.pause(0.2)

    if fx(a) * fx(b) > 0:
        print('No solution exist.')
        break

    if fx(a) * fx(x) < 0:
        b = x
    else:
        a = x

print(tb.tabulate(ans, headers=['a(-)', 'b(+)', 'x', 'y'], tablefmt='orgtbl', showindex='always'))
plt.show()
