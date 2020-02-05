from tabulate import *

m = [
    [10, 5, 2, 40],
    [5, 15, 2, 53],
    [4, 6, 22, 45]
]

fx = lambda a, b, c: round((m[0][0] * a + m[0][1] * b + m[0][2] * c), 4) == m[0][-1]

a = b = c = 1.5

x1 = lambda b, c: (m[0][3] - m[0][1] * b - m[0][2] * c) / m[0][0]
x2 = lambda a, c: (m[1][3] - m[1][0] * a - m[1][2] * c) / m[1][1]
x3 = lambda a, b: (m[2][3] - m[2][0] * a - m[2][1] * b) / m[2][2]

ans = []

while not fx(a, b, c):
    a = x1(b, c)
    b = x2(a, c)
    c = x3(a, b)

    ans.append([a, b, c])

print(tabulate(ans, headers=['x1', 'x2', 'x3'], tablefmt='orgtbl', showindex='always'))
