# Question 20:Take a word as input and doubles its each letter, store and display the result.

word = input('Enter a word: ')
new_word = ''

for letter in word:
    new_word += letter*2

print('output: ', new_word)