# Создайте программу для игры с конфетами человек против человека, ченловек против бота

from random import randint as rd

sum = 117
part = [1, 2]

i = rd(0, 1)
game = True
while game == True:
    if i == 2 or i == 0:
        i = 0
        x = rd(1, 28)
        print(x)
    else:
        x = int(input(f'Participant {part[1]}, take 1-28 bonbons: '))
    if x < 1 or x > 28:
        x = int(input('Wrong number. Input 1-28 num: '))
    sum -= x
    if sum <= 28:
        if i == 1:
            print('Congrats - you won!')
        else:
            print('Bot won!')
        print(f'sum = {sum}')
        game = False
    i += 1

    