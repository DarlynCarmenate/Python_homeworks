# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def pairs_pow(arr):
    list_2 = []
    j = -1

    if len(arr) % 2 == 0:
        length = len(arr) //2
    else:
        length = len(arr) //2 + 1

    for i in range (length):
        list_2.append(arr[i] * arr[j])
        j -= 1
    return (list_2)


list_1 = [3, 5, 3, 7, 5, 2, 1]
print(pairs_pow(list_1))