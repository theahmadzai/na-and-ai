import tabulate as tb
import numpy as np
import matplotlib.pyplot as plt

fx = lambda x: 1 / (1 + x ** 2)

# lower, upper limits, slices and width
l = 2
u = 5
n = 7
w = abs(l - u) / n

# plot function
xPoints = np.linspace(l, u)
yPoints = fx(xPoints)
plt.plot(xPoints, yPoints, color='orange')

# n no of x points
XS = np.linspace(l, u, n + 1)

ans = []

area = 0

for i in range(n):
    # plot trapezoid
    print(XS[i], XS[i + 1])
    plt.fill([XS[i], XS[i], XS[i + 1], XS[i + 1]], [0, fx(XS[i]), fx(XS[i + 1]), 0], color='blue', edgecolor='black',
             alpha=0.5)
    plt.pause(0.002)

    # append to ans array
    ans.append([XS[i], 2 * fx(XS[i])])

    # sum integrated area
    area += 2 * fx(XS[i])

area = (area - fx(XS[0]) + fx(XS[-1])) * w / 2

print(tb.tabulate(ans, headers=['x', 'fx(x)'], tablefmt='orgtbl', showindex='always'))
print('Integrated area: ', area)

plt.title('Trapezoidal Rule, N = {}'.format(n))
plt.show()
