# Question 12:Write a program to print Factors of a number

n = int(input('Number: '))

for i in range(1, (n//2)+1):
    if n%i == 0:
        print(i)
