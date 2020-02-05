from math import e
import numpy as np
import matplotlib.pyplot as plt

# f = lambda x: e**x - 6
# f = lambda x: x**2 + x**3 + x**4 - 6

X = np.linspace(0, 14, 15)
Y = np.random.randint(0, 100, 15)
plt.scatter(X,Y, color='orange')

_x = 0
_y = 0
_x_y = 0
_x2 = 0
_x3 = 0
_x4 = 0
_x2_y = 0

for x,y in zip(X,Y):
    _x += x
    _y += y
    _x_y += x*y
    _x2 += x**2
    _x3 += x**3
    _x4 += x**4
    _x2_y += (x**2)*y

#y = ax + bn
#xy = axx + bx
#45 = 55b + 10a
#274 = 385a + 55b
A = np.array([
    [_x,    len(X)],
    [_x2,   _x]
])
B = np.array([_y, _x_y])
L = np.linalg.solve(A,B)

linear = lambda x: L[0]*x + L[-1]
plt.plot(X, [linear(n) for n in X], color='green')

A = np.array([
    [_x4,   _x3,    _x2],
    [_x3,   _x2,    _x],
    [_x2,   _x,     _x]
])
B = np.array([_x2, _x_y, _y])
P = np.linalg.solve(A,B)

parabola = lambda x: P[0]*(x**2) + P[1]*x + P[2]
plt.plot(X,[parabola(n) for n in X], color='blue')

plt.show()
