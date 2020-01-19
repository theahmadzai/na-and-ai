# Question 28:Delete the 50 elements of the random generated list.

from random import randint

numbers = [randint(0,100) for i in range(10)]

print('List: ', numbers)

print('First 50% Deleted: ', numbers[len(numbers)//2:])