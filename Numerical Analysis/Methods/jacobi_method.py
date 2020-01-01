from tabulate import *

a = b = c = d = 1.5

x1 = lambda b,c: (1/4 - 1/4*b - 1/4*c)/1
x2 = lambda c,d: (1/4 - 1/4*c - 1/4*d)/1
x3 = lambda a,c: (1/2 - 1/4*a - 1/4*c)/1
x4 = lambda a,b: (1/2 + 1/4*a - 1/4*b)/1

ans = []

for i in range(13):
    w = x1(b,c)
    x = x2(c,d)
    y = x3(a,c)
    z = x4(a,b)


    ans.append([i,w,x,y,z])

    a = w
    b = x
    c = y
    d = z

print(tabulate(ans, headers=['k', 'x1', 'x2', 'x3'], tablefmt='orgtbl'))
