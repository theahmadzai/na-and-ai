import tabulate as tb
import numpy as np
import matplotlib.pyplot as plt

fx = lambda x: (x ** 3) - (3 * x) - 5
sfx = lambda a, b: (a * fx(b) - b * fx(a)) / (fx(b) - fx(a))

# plot function
X = np.linspace(-10, 10, 1000)
Y = fx(X)
plt.plot(X, Y, color='orange')

a = -2
b = 7

ans = []

while round(fx(a), 4) != 0:
    # append result row to ans array
    ans.append([round(a, 4), round(fx(a), 4)])

    # plot secent line
    plt.plot([a, b], [fx(a), fx(b)], color='red')
    plt.pause(0.2)

    a, b = b, sfx(a, b)

print(tb.tabulate(ans, headers=['xn', 'y'], tablefmt='orgtbl', showindex='always'))
plt.show()
