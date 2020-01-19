# Question 29:delete the last 50 elements of random generated list

from random import randint

numbers = [randint(0,100) for i in range(10)]

print('List: ', numbers)

print('Last 50% Deleted: ', numbers[:len(numbers)//2])