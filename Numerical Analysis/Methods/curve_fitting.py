from math import e
import numpy as np
import matplotlib.pyplot as plt

f = lambda x: e**x - 6

xs = np.linspace(-5,5,1000)
ys = f(xs)

_x = 0
_y = 0
_x_y = 0
_x_square = 0

for x,y in zip(xs,ys):
    _x += x
    _y += y
    _x_y += x*y
    _x_square += x*x

#y = ax + bn
#xy = axx + bx
#45 = 55b + 10a
#274 = 385a + 55b
A = np.array([[_x, len(xs)], [_x_square,_x]])
B = np.array([_y, _x_y])
D = np.linalg.inv(A)
E = np.dot(D,B)

linear = lambda x: (E[0]*x) + E[-1]

print(_x,_y,_x_y,_x_square)
plt.plot(xs,ys, color='orange')

yss = [linear(i) for i in xs]
print(xs, ys, yss)
plt.plot(xs,yss, color='green')

plt.show()
