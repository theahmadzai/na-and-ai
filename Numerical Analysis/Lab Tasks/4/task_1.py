numbers = dict()

n = int(input('How many values do you want?: '))

for i in range(1, n+1):
    numbers[i] = int(input("Number: "))


c = None

while(c not in ('exit', 'quit')):
    n = int(input('Which key to remove?: '))

    if n in numbers.keys():
        del numbers[n]
        print('removed key ' + str(n) + ' from dict')
    else:
        print('Key does not exist in dict')

    c = input('To close program type: (quit,exit): ')

ans = 1

for n in numbers:
    ans *= numbers[n]

print("Product of dict: " + str(ans))

ans = 0

for n in numbers:
    ans += numbers[n]

print("Sum of dict: " + str(ans))

