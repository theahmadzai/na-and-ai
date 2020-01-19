# Question 4:Write a code to solve the quadratic  formula (-b*sqrt((b**2)-4*a*c))/2*a

from math import sqrt

a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

print('Answer: for -i', ((-b*sqrt((b**2)-4*a*c))/2*a), ' for +i', ((-b*-sqrt((b**2)-4*a*c))/2*a))