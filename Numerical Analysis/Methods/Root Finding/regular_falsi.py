import tabulate as tb
import numpy as np
import matplotlib.pyplot as plt

fx = lambda x: (x ** 3) - (3 * x) - 5
sfx = lambda a, b: (a * fx(b) - b * fx(a)) / (fx(b) - fx(a))

# plot function
X = np.linspace(-10, 10,1000)
Y = fx(X)
plt.plot(X,Y, color='orange')

a = -5.5
b = 7

ans = []

while round(fx(a), 4) != 0:
    x = sfx(a, b)

    # append result row to ans array
    ans.append([round(a, 4), round(b, 4), round(x, 4), round(fx(x), 4)])

    # plot secant line
    plt.plot([a, b], [fx(a), fx(b)], color='red')
    plt.pause(0.1)

    # plot secant point
    plt.plot(x, sfx(a,b), marker='o', markersize=3, color='green')
    plt.pause(0.1)

    if fx(a) * fx(b) > 0:
        print('No solution exist.')
        break

    if fx(a) * fx(x) < 0:
        b = x
    else:
        a = x

print(tb.tabulate(ans, headers=['a(-)', 'b(+)', 'x', 'y'], tablefmt='orgtbl', showindex='always'))
plt.show()
