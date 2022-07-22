# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

lst = input('Enter a list of numbers: ').split()
lst_2 = []
for i in lst:
    if i not in lst_2:
        lst_2.append(i)
        print(i)
print(lst_2)