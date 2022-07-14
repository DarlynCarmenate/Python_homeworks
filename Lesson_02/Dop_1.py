# Вклад в банке составляет X рублей. Ежегодно он увеличивается на P процентов, 
# после чего дробная часть копеек отбрасывается.Требуется определить: 
# через сколько лет вклад составит не менее Y рублей.

from calendar import month
import math

x = float(input('Введите размер вклада: '))
p = float(input('Введите процент: '))
y = float(input('Введите желаемую итоговую сумму: '))

months = 1
while x < y:
    per = x*(p/100/12)
    x += per
    print(f'{months} - {per}, {x}')
    months += 1  
years = months / 12
print(math.ceil(years))