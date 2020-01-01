teams = {}

choice = None

while choice not in ('quit','exit'):
    name = input('Team name: ')
    wins = int(input('Team wins: '))
    loses = int(input('Team loses: '))

    teams[name] = [wins,loses]

    choice = input('To quit type: (quit,exit): ')

choice = None

while choice not in ('quit','exit'):
    name = input('Team name to check win rate: ')

    if name not in teams:
        print('Invalid team!')
    else:
        print('Winrate: ' + str((teams[name][0]/(teams[name][0]+teams[name][1]))*100) + '%')

    choice = input('To quit type: (quit,exit): ')

records = [team for team in teams if teams[team][0] != 0]

print('Records: ', records)
