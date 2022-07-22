# Задайте натуральное число N. Напишите программу, которая составит список 
# простых делителей числа N. (1 - составное число)

from re import I


n = int(input('Input number n: '))
for i in range(2, n + 1):
   if n % i == 0:
    print(i)
