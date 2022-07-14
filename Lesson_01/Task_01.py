# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

day_num = int(input('Input the day number: '))

if day_num < 0 or day_num > 7:
    print("There's no such a day")
elif day_num > 0 and day_num < 6:
    print('Workday')
else:
    print('Weekday') 