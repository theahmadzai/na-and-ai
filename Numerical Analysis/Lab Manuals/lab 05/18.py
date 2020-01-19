# Question 18:write multiplication game program for kids the program should give the player ten randomly generated
# multiplication question to do. After each program should tell them whether they got its right or wrong and
# what is the correct answer is.

from random import randint, choice

correct_answers = 0

for i in range(1,8):
    a = randint(5,25)
    b = choice(['*', '/', '+', '-'])
    c = randint(0,10)

    question = str(a) + str(b) + str(c)
    answer = 0

    if b == '*':
        answer = a * c
    elif b == '/':
        answer = a / c
    elif b == '+':
        answer = a + c
    else:
        answer = a - c

    print('-------------\nQ#' + str(i) + ': ' + question)

    ans = input("Answer: ")

    if float(ans) == answer:
        correct_answers += 1
    else:
        print('Wrong Answer, correct answer is: ' + str(answer))

    print('Correct Answers: ' + str(correct_answers))
    print('Percentage: ' + str((correct_answers/i)*100))
