# Question 17:write a program that prints out the sine and cosine of the angle ranging
# from 0 to 346 in 15 increment each result should should be rounded to 4 decimal places.

from math import sin, cos, radians

for i in range(0, 346, 15):
    print('Sin: ', round(sin(radians(i)),4), '\tCos: ', round(cos(radians(i)),4))