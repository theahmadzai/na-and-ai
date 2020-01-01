from math import *
from random import *

t = input('Enter temprature (value(unit)): ')
v = float(t[:-1])
u = t[-1]
r = 0

if u == 'f':
    r = 5/9*(v-32)
    u = 'c'
elif u == 'c':
    r = (9/5)*v+32
    u = 'f'
else:
    print("Wrong Unit!")
    exit()

print("Temprature: " + str(round(r, 2)) + u)