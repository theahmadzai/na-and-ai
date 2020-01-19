import numpy as np
import matplotlib.pyplot as plt

f = lambda x: 1/(1 + x**2)

a = 0 # Starting value
b = 5 # Ending value
N = 100 # No of shapes
h = abs(b-a) / N

xp = [i for i in np.arange(a,b+h,h)]
yp = [f(i) for i in xp]

plt.plot(xp, yp, color='orange')

#x and y values for the rectengular rule
x = np.linspace(a,b,N+1)
y = f(x)

# X and Y values for plotting y = f(x)
X = np.linspace(a,b,1000)
Y = f(X)

plt.plot(X,Y)

for i in range(999):
    xs = [X[i], X[i], X[i+1], X[i+1]]
    ys = [0, f(X[i]), f(X[i+1]), 0]

    # plt.fill(xs, ys, 'm', edgecolor='black', alpha=0.05)

for i in range(N):
    xs = [x[i], x[i], x[i+1], x[i+1]]
    ys = [0, f(x[i]), f(x[i]), 0]

    plt.fill(xs, ys, 'm', edgecolor='black', alpha=0.5)

plt.title('Rectangular Rule, N = {}'.format(N))
plt.show()


s = 0
for i in yp:
    s+= i

s = s*h