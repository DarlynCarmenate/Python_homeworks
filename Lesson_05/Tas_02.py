# Создайте программу для игры в ""Крестики-нолики""

from random import randint as rd

arr = [['1', '2', '3'], 
       ['4', '5', '6'], 
       ['7', '8', '9']]
for i in arr:
    print(*i)

count = 0
end = False
while end == False:
    if count % 2 == 0:
        print('Cross turn')
        x = int(input('Input x: '))
        y = int(input('Input y: '))
        arr[x - 1][y - 1] = 'X'
        for i in arr:
            print(*i)
        count += 1
    else:
        print('Zero turn')
        x = int(input('Input x: '))
        y = int(input('Input x: '))
        arr[x - 1][y - 1] = 'O'
        for i in arr:
            print(*i)
        count += 1
    if count >= 4:
        if arr[0][0] == arr[0][1] == arr[0][2] or arr[1][0] == arr[1][1] == arr[1][2] or \
        arr[2][0] == arr[2][1] == arr[2][2] or arr[0][0] == arr[1][0] == arr[2][0] or \
        arr[0][1] == arr[1][1] == arr[2][1] or arr[0][2] == arr[1][2] == arr[2][2] or \
        arr[0][0] == arr[1][1] == arr[2][2] or arr[0][2] == arr[1][1] == arr[2][0]:
            if count % 2 == 1:
                print('Cross won!')
            else:
                print('Zero won!')
            end = True
        elif count == 9:
            print('Dead heat')
            end = True

    

    

