# Question 24:Print the first and second largest and smallest no of random generated list.

from random import randint

numbers = [randint(0,100) for i in range(10)]

print('List: ', numbers)

first_min = min(numbers)
second_min = min([n for n in numbers if n != first_min])
first_max = max(numbers)
second_max = max([n for n in numbers if n != first_max])

print('First min: ', first_min)
print('Second min: ', second_min)
print('First max: ', first_max)
print('Second max: ', second_max)
