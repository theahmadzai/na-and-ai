# Question 19:Write a program that ask the user for string and print out the location of the asked letter.

words = input('Enter a string: ')
letter = input('Enter a letter: ')

if letter in words:
    print(words.index(letter))
else:
    print('Letter: ', letter, ' not in entered string.')