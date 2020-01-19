#Question 3:Take the starting point  and ending point and number from user and display the table of that number?

s = int(input('Starting point: '))
e = int(input('Ending point: '))
n = int(input('Enter number: '))

for i in range(s, e+1):
    print(n, ' X ', i, ' = ', i * n)