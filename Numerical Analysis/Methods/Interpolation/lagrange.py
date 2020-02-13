import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

x = [1, 7,10,15,70,85]
y = [50,-3,8,50,-50,10]

plt.scatter(x,y)

poly = lagrange(x, y)

X=np.linspace(x[0],x[-1])
Y=poly(X)

plt.plot(X,Y)
plt.show()