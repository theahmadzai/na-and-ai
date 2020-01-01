from tabulate import *

p = [1, -1, -12]


def fx(p, i):
    d = []
    j = 0

    for n in p:
        d.append(n + j)
        j = d[-1] * i

    return d


def fdx(p, i):
    return fx(p[:-1], i)


n = 2

ans = []

for i in range(5):
    _fx = fx(p, n)
    _fdx = fdx(_fx, n)
    n -= _fx[-1] / _fdx[-1]

    ans.append([i, n])

print(tabulate(ans, headers=['n', 'xn'], tablefmt='orgtbl'))
