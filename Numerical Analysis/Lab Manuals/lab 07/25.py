# Question 25:Print the even and odd no of the random generated list

from random import randint

numbers = [randint(0,100) for i in range(10)]

print('List: ', numbers)

print('Even list: ', [n for n in numbers if n%2 == 0])
print('Odd list: ', [n for n in numbers if n%2 != 0])
