# Напишите программу, которая принимает на вход координаты двух точек и находит 
# расстояние между ними в 2D пространстве.

import math

x1 = int(input('Input x1: '))
x2 = int(input('Input x2: '))
y1 = int(input('Input y1: '))
y2 = int(input('Input y2: '))

sqrt = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(round(sqrt, 2))