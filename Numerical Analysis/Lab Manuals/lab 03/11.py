# Question 11:Write a program to print Fibonacci  series of a number.

n = int(input('Number: '))

a = 0
b = 0
c = 1
for i in range(n+1):
    a = b
    b = c
    c = a + b
    print(a)