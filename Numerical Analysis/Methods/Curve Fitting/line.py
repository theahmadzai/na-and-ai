import tabulate as tb
import numpy as np
import matplotlib.pyplot as plt

xPoints = [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]  # np.linspace(0, 14, 15)
yPoints = [2, 6, 7, 8, 10, 11, 11, 10, 9]  # np.random.randint(0, 100, 15)
plt.scatter(xPoints, yPoints, color='orange')

_n = len(xPoints)
_x = 0
_y = 0
_xy = 0
_x2 = 0

ans = []

for x, y in zip(xPoints, yPoints):
    _x += x
    _y += y
    _xy += x * y
    _x2 += x ** 2

    # append to ans array
    ans.append([x, y, x * y, x ** 2])

# append summations
ans.append(['---', '---', '---', '---', '---', '---', '---'])
ans.append([_x, _y, _xy, _x2])
print(tb.tabulate(ans, headers=['_x', '_y', '_xy', '_x2'], tablefmt='orgtbl', showindex='always'))

# _y = a*_x + b*n
# _xy = a*_x2 + b*_x
A = np.array([
    [_x, _n],
    [_x2, _x]
])
B = np.array([_y, _xy])
L = np.linalg.solve(A, B)

line = lambda x: L[0] * x + L[1]

plt.plot(xPoints, [line(n) for n in xPoints], color='green')
plt.title('Line fitting')
plt.show()
