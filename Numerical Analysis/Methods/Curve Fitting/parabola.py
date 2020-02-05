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
_x2y = 0
_x2 = 0
_x3 = 0
_x4 = 0

ans = []

for x, y in zip(xPoints, yPoints):
    # calculate summations
    _x += x
    _y += y
    _xy += x * y
    _x2y += (x ** 2) * y
    _x2 += x ** 2
    _x3 += x ** 3
    _x4 += x ** 4

    # append to ans array
    ans.append([x, y, x * y, (x ** 2) * y, x ** 2, x ** 3, x ** 4])

# append summations
ans.append(['---', '---', '---', '---', '---', '---', '---'])
ans.append([_x, _y, _xy, _x2y, _x2, _x3, _x4])
print(tb.tabulate(ans, headers=['_x', '_y', '_xy', '_x2y', '_x2', '_x3', '_x4'], tablefmt='orgtbl', showindex='always'))

# solve equations
# _y = a*_x2 + b*_x + c*n
# _xy = a*_x3 + b*_x2 + c*_x
# _x2y = a*_x4 + b*_x3 + c*_x2
A = np.array([
    [_x2, _x, _n],
    [_x3, _x2, _x],
    [_x4, _x3, _x2]
])
B = np.array([_y, _xy, _x2y])
P = np.linalg.solve(A, B)

parabola = lambda x: (P[0] * (x ** 2)) + (P[1] * x) + P[2]

plt.plot(xPoints, [parabola(n) for n in xPoints], color='green')
plt.title('Parabolic fitting')
plt.show()
