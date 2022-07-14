# Напишите программу, которая принимает на вход число N и выдает набор 
# произведений чисел от 1 до N. Факториал

n = int(input('Input a number: '))
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)