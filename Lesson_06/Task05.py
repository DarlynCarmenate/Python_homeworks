# Напишите функцию same_by(caracteristic, objects), которая проверяет, 
# все ли объекты имеют одинаковое значение некоторой характеристики, и возвращает
# True, если это так. Для пустого набора объектов возвращает True. caracteristic - 
# это функция, которая принимает обхекст и вычисляет его характеристику.

values = [0, 2, 6, 8]

def same_by(caracteristic, objects):
    a = [caracteristic(i) for i in objects]
    return a

if same_by(lambda x: x % 2 == 0, values):
    print('same')
else:
    print('different') 