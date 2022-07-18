# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def decim_binary(n):
    binar = ''
    while n > 0:
        binar = str(n % 2) + binar
        n //= 2
    return(binar)


num = int(input('Input a number: '))
print(decim_binary(num))