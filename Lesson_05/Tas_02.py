# Создайте программу для игры в ""Крестики-нолики""

from random import randint as rd

arr = [['*', '*', '*'], 
       ['*', '*', '*'], 
       ['*', '*', '*']]
for i in arr:
    print(*i)

count = 0
end = False
while end == False:
    if count % 2 == 0:
        part = 'X'
        print('Cross turn')
    else:
        part = 'O'
        print('Zero turn')
    x = int(input('Input x: '))
    y = int(input('Input y: '))
    if arr[x - 1][y - 1] == part:
        print('Already busy! You skip..')
    elif arr[x - 1][y - 1] == '*':
        arr[x - 1][y - 1] = part
    for i in arr:
        print(*i)
    count += 1
    if count >= 4:
        if arr[0][0] == arr[0][1] == arr[0][2] != '*' or arr[1][0] == arr[1][1] == arr[1][2] != '*' or \
        arr[2][0] == arr[2][1] == arr[2][2] != '*' or arr[0][0] == arr[1][0] == arr[2][0] != '*' or \
        arr[0][1] == arr[1][1] == arr[2][1] != '*' or arr[0][2] == arr[1][2] == arr[2][2] != '*' or \
        arr[0][0] == arr[1][1] == arr[2][2] != '*' or arr[0][2] == arr[1][1] == arr[2][0] != '*':
            if count % 2 == 1:
                print('Cross won!')
            else:
                print('Zero won!')
            end = True
        elif count == 9:
            print('Dead heat')
            end = True

