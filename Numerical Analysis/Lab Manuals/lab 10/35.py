# Question 35: Write python code for Seidal method for equation
# 12x1 + 2x2 + 2x3 = 5
# 2x1 + 15x2 + x3 = 5
# 3x1 + 2x2 + 25x3 = 5

from tabulate import *
import matplotlib.pyplot as plt

m = [
    [12, 2, 2, 5],
    [2, 15, 1, 5],
    [3, 2, 25, 5]
]

a = b = c = 1.5

check = lambda x1,x2,x3: (12*x1 + 2*x2 + 2*x3) == 5

x1 = lambda b,c: (m[0][3] - m[0][1]*b - m[0][2]*c)/m[0][0]
x2 = lambda a,c: (m[1][3] - m[1][0]*a - m[1][2]*c)/m[1][1]
x3 = lambda a,b: (m[2][3] - m[2][0]*a - m[2][1]*b)/m[2][2]

ans = []

while not check(a,b,c):
    a = x1(b,c)
    b = x2(a,c)
    c = x3(a,b)

    ans.append([a,b,c])

print(tabulate(ans, headers=['x1', 'x2', 'x3'], tablefmt='orgtbl', showindex='always'))
plt.scatter([a,b,c],[x1(b,c), x2(a,c), x3(a,b)], color='black')
plt.show()