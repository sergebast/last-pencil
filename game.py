from random import randint

players = ['John', 'Jack']


def bot_step(q):
    if q == 1:
        return 1
    else:
        pen = q % 4
        if pen == 0:
            return 3
        elif pen == 2:
            return 1
        elif pen == 3:
            return 2
        else:
            return randint(1, 3)


while True:
    try:
        pencil = int(input('How many pencils '))
        if pencil == 0:
            print('The number of pencils should be positive')
        elif pencil < 0:
            print('The number of pencils should be numeric')
        else:
            break
    except ValueError:
        print('The number of pencils should be numeric')

while True:
    player = input('Who will be the first (John, Jack) ')
    if player in players:
        break
    print('Choose between', players[0], 'and', players[1])

print('|' * pencil)

while pencil > 0:
    print(player + '\'s', 'turn:')
    if player == 'Jack':
        x = bot_step(pencil)
        print(x)
    else:
        while True:
            try:
                x = int(input())
                if x > 3 or x <= 0:
                    print("Possible values: '1', '2' or '3'")
                elif x > pencil:
                    print('Too many pencils were taken')
                else:
                    break
            except ValueError:
                print("Possible values: '1', '2' or '3'")
    pencil -= x
    print('|' * pencil)
    if player == 'John':
        player = 'Jack'
    else:
        player = 'John'
else:
    print(player, 'won!')
