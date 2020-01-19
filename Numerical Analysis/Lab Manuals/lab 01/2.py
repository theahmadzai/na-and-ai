#Question 2: Display the table of the number that user enter?

n = int(input('Enter a number: '))

for i in range(1, 11):
    print(n, ' X ', i, ' = ', i*n)