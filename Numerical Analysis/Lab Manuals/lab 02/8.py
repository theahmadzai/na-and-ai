# Question 8:Write a program to display the following  Shape.
#   *
#  ***
#   *

for i in [1,3,1]:
    if i != 3:
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print('')