import numpy as np
import matplotlib.pyplot as plt

fx = lambda x: 1 / (1 + x ** 2)

a = 0  # lower limit
b = 5  # upper limit

n = 10  # slices
h = abs(b - a) / n  # width

# plot function
X = np.linspace(a, b, n)
Y = fx(X)
plt.plot(X, Y, color='orange')

XS = np.linspace(a, b, n + 1)
YS = fx(XS)
plt.plot(XS, YS, color='blue')

area = 0
for i in range(n):
    # plot rectangle
    plt.fill([XS[i], XS[i], XS[i + 1], XS[i + 1]],
             [0, fx(XS[i]), fx(XS[i]), 0],
             color='blue', edgecolor='black', alpha=0.5)
    plt.pause(0.2)

    # sum integrated area
    area += Y[i] * h

print('Integrated area: ', area)
plt.title('Rectangular Rule, N = {}'.format(n))
plt.show()
