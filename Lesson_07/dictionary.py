from russian_names import RussianNames as rn
from random import randint as rd

def create_dict():
    lst = ['Москва', 'Адлер', 'Сочи', 'СПб', 'Москва', 'Чита', 'Омск', 'Ейск', 'Тверь', 'Тула']
    d = dict()
    for i in range(10):
        d[i] = rn(patronymic = False).get_person(), f'+7-{rd(200, 500)}-{rd(100000000,199999999)}', lst[i] 
    return d

d = create_dict()
