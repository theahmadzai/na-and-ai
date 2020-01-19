# Question 23:Generate a list of size 100 between (0,101).Print the generated list sort the list
# and print the sorted list .create a new list and find frequency of each element of a list

from random import randint
from pprint import pprint

numbers = [randint(0,101) for x in range(100)]
print('List: ', numbers)

numbers.sort()
print('Sorted: ', numbers)

frequency = {}

for n in numbers:
    if n not in frequency:
        frequency[n] = 1
    else:
        frequency[n] += 1

print('Frequency: ')
pprint(frequency)