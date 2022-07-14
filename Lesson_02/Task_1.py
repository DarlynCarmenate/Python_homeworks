# Напишите программу, которая принимает на вход вещественное число и показывает 
# сумму его цифр.

from dataclasses import replace


n = input('Input a float number: ')
point = n.replace('.', '')
num = int(point)
sum = 0
for i in range(num):
    sum += num % 10
    num //= 10
print(sum)


