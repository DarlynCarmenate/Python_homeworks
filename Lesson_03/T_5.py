# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

k = int(input('Input k: '))
n = [0]
n1, n2 = 0, 1
f1, f2 = 0, 1
for i in range(k):
    (n1, n2) = (n2, n1 + n2)
    n.append(n1)
    (f1, f2) = (f2, f1 + f2 * -1)
    n.insert(0, f1)
print(n, end=' ')