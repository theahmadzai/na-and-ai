# Question 14:write a program  that generate random  number  x between  1 and 50 and
# random number y between 2 and 5 and computes x pow y

from random import randint

x = randint(1,50)
y = randint(2,5)

print(x**y)