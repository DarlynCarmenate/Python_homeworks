# Вычислить число пи c заданной точностью d

from decimal import Decimal
from decimal import getcontext

n = int(input('Input number of pi digits: '))

def pi_num(d: int):
    pi = 0
    getcontext().prec=d
    for i in range(d):
        pi += 1/Decimal(16)**i *(Decimal(4)/(8*i+1) - 
         Decimal(2)/(8*i+4) - Decimal(1)/(8*i+5) -
         Decimal(1)/(8*i+6))
    return pi

print(pi_num(n))
