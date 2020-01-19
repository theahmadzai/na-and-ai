# Question 26:Print the sorted list in reverse order

from random import randint

numbers = [randint(0,100) for i in range(10)]

print('List: ', numbers)

numbers.sort()
print('Sorted: ', numbers)

numbers.reverse()

print('Reversed: ', numbers)