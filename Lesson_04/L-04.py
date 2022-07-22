# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и вывести на экран.

import random
import string

k = int(input('Задайте степень k: '))
result = ''
while k > 0:
    result += f'{random.choice(string.ascii_lowercase)} * x ** {k} + '
    k -= 1
if k == 1:
    result += f'{random.choice(string.ascii_lowercase)} * x + '
if k == 0:
    result += random.choice(string.ascii_lowercase)
print(result)