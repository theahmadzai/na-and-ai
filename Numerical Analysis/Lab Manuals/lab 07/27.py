# Question 27:Double the size of the random list ,store it, display/print it

from random import randint

numbers = [randint(0,100) for i in range(10)]

print('List: ', numbers)

print('Doubled: ', numbers*2)