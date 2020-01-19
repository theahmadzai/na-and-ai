# Question 22:Write a program that remove the following punctuation from user asked string[, ; : > < - _ / \ . @]
# input string=AB,C;DE><FG@
# output=ABCDEGF

p = ',;:><-_/\\.@'

word = input('Enter a string: ')
new_word = ''

for letter in word:
    if letter not in p:
        new_word += letter

print(new_word)