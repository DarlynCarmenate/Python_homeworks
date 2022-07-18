# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.

def min_max(fl_list):
    max = fl_list[0] % 1
    min = fl_list[0] % 1
    for i in range(len(fl_list)):
        if fl_list[i] % 1 == 0:
            continue
        elif fl_list[i] % 1 > max:
            max = fl_list[i] % 1
        elif fl_list[i] % 1 < min:
            min = fl_list[i] % 1
    return(round(max - min, 2))

float_list = [1.2, 4.5, 5, 1.1, 4.02, 3.12, 3.05]
print(min_max(float_list))