from random import *

numbers = [randint(0,10) for i in range(10)]

numbers.sort()

frequency = {}

fmin = numbers[-1]
smin = numbers[-2]
fmax = 0
smax = 0

for n in numbers:

    if n not in frequency:
        frequency[n] = 1
    else:
        frequency[n] += 1

    if fmin > n:
        fmin = n

    if smin > n:
        if fmin != n:
            smin = n

    if fmax < n:
        fmax = n

    if smax < n:
        if fmax != n:
            smax = n

print(numbers)
print(frequency)

#2
print('First min: ', fmin)
print('Second min: ', smin)
print('First max: ', fmax)
print('Second max: ', smax)

#3
print('Even List: ', [i for i in numbers if i%2==0])
print('Even List: ', [i for i in numbers if i%2!=0])

#4
r = numbers.copy()
r.reverse()
print('Reverse List: ', r)

#5
print('Double List: ', numbers * 2)

#6
d = numbers.copy()
d = d[:len(d)//2]
print('First 50% of List: ', d)

#7
d = numbers.copy()
d = d[len(d)//2:]
print('Last 50% of List: ', d)