# Question  13:Write a program that add * in equation .

eq = input('Equation: ')
new_eq = ''

for i, e in enumerate(eq):
    if e.isalpha() and i != 0:
        new_eq += '*'
    new_eq += e

print(new_eq)
