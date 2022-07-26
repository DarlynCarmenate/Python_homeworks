# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

list1 = input('Input a string for RLE, each item throught space: ').split()
list2 = list()
letter = ''
count = 1
for i in range(len(list1) - 1):
    if list1[i] == list1[i + 1]:
        count += 1
        letter = list1[i]
    if list1[i] != list1[i + 1]:      
        list2.append(list1[i])
        list2.append(count)
        count = 1
list2.append(list1[i])
list2.append(count)
rle_final = ' '.join(map(str, list2)) 
print(rle_final)

list3 = rle_final.split()
list4 = list()
for i in range(0, len(list3), 2):
    list4.append(list3[i] * int(list3[i + 1]))
print(''.join(list4))