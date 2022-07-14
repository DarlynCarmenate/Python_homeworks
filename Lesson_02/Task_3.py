# # Задана последовательность натуральных чисел, завершающаяся числом 0. 
# # Требуется определить значение второго по величине элемента в этой последовательности

list = [1, 7, 9, 0]
max1 = list[0]
max2 = list[1]

for i in range(len(list)):
    if (list[i] > max1): 
        max1 = list[i]
        print(max1)
    if (list[i] > max2 and list[i] < max1):
        max2 = list[i]
        print(max2)
print(max2)

list = [1, 7, 9, 0]
max1=max(list)
list.remove(max1)
max2=max(list)
print(max2)