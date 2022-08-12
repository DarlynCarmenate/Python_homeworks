# Создать калькулятор для работы с рациональными и комплексными числами, 
# организовать меню, добавив в неё систему логирования

from decimal import Decimal 
import re
from Task_2_log import *


def calc(message):
    mes = list()
    mes = re.split('\s+', message)
    if len(mes) == 3:
        item1 = Decimal(mes[0])
        item2 = Decimal(mes[2])
        oper = mes[1]
        print(item1, item2, oper)
        out = str(ration_oper(item1, item2, oper))
        print(out)
        return out
    if len(mes) == 7:
        print(mes[0], mes[1], mes[2], mes[4], mes[5], mes[6], mes[3])
        item1 = complex(mes[0] + mes[1] + mes[2])
        item2 = complex(mes[4] + mes[5] + mes[6])
        oper = mes[3]
        print(item1, item2, oper)
        out = str(complex_oper(item1, item2, oper))
        print(out)
        return out
    return 'Ошибка ввода'
        

def ration_oper(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '*':
        return a * b
    elif operation == '-':
        return a - b
    elif operation == '/':
        return a / b

def complex_oper(a, b, operation):
    if operation == '+':
        return complex(a + b)
    elif operation == '*':
        return complex(a * b)
    elif operation == '-':
        return complex(a - b)
    elif operation == '/':
        return complex(a / b)

# calc('3.7 + 2.5')
# print(calc('1.1 +   2j  +    2.2  + 3j'))
