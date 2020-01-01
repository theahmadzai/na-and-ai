from math import *
from random import *

options = ('r', 'p', 's')
against = {
    'r': 'p',
    'p': 's',
    's': 'r'
}
winrate = 0
wins = 0

namify = {
    'r': 'Rock',
    's': 'Scissor',
    'p': 'Paper'
}

for i in range(1,6):
    x = choice(options)
    print("*********** ROUND " + str(i) + "***********")
    y = input("Enter choice? ")

    if against[x] == y:
        wins += 1
        print("WIN!")
        print("You clever, " + namify[y] + " defeated " + namify[x])
    elif x == y:
        print("DRAW!")
        print("You both chose, " + namify[x])
    else:
        print("LOSE!")
        print("Only " + namify[against[x]] + " can defeat " + namify[x] + " but you chose " + namify[y])

    winrate = (wins/i)*100
    print("Your win rate is: " + str(winrate))

