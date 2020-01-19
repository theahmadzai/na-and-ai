# Question 21: input name=yasir
# OUTPUT=y ya yas yasi yasir

name = input('Enter name: ')

for i in range(len(name)):
    print(name[:i+1], end=' ')