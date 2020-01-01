from math import *
from tabulate import *

se = lambda a, b: ((a * ((e ** (2 * b)) - 6)) - (b * ((e ** (2 * a)) - 6))) / ((e ** (2 * b)) - (e ** (2 * a)))
fx = lambda x: (e ** (2 * x)) - 6

a = 0.5
b = 1

ans = []

for i in range(7):
    x = se(a, b)

    ans.append([i, round(a, 4), round(b, 4), round(x, 4), round(fx(x), 4)])

    if fx(a) * fx(b) > 0:
        print('No solution exist.')
        break

    if fx(a) * fx(x) < 0:
        b = x
    else:
        a = x

print(tabulate(ans, headers=['n', 'a(-)', 'b(+)', 'mean', 'f(mean)'], tablefmt='orgtbl'))
