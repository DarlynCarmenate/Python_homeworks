# Создать информационную систему позволяющую работать с сотрудниками
# некой компании \ студентами вуза \ учениками школы

database = {}
db = {'parents': 1, 'children': 2, 'payments': 3}

def reading_file_to_dict(number_file):
    with open(f'{number_file}.txt', 'r', encoding='utf-8') as file_1:
        data = [i.split('\n')[0] for i in file_1.readlines()]
        # print(data)
        database[number_file] = []
        for i in data:
            database[number_file].append(tuple(i.split(';')))

#Найти детей по фамилии родителя
def print_children(second_name):
    id = [i[0] for i in database[db['parents']] if second_name in i][0]
    deti = [i for i in database[db['children']] if id == i[1]]
    print(*[' '.join(i[2:4]) + '\n' for i in deti])

#Вывести: родителей не оплативших, их телефоны
def payment_status():
    summ = [i[1] for i in database[db['payments']] if 'no' in i or 'part' in i]
    phone = [i for i in database[db['parents']] if i[0] in summ]
    print(*[' '.join(i[1:]) + '\n' for i in phone])

#По фамилии родителя удалить всю инфо по родителю и всем его детям
def delete_info(parent_surname):
    id = [i[0] for i in database[db['parents']] if parent_surname in i][0]
    newtable = [i for i in database[db['parents']] if id !=  i[0]]
    newtable2 = [i for i in database[db['children']] if id != i[1]]
    database[db['parents']] = newtable
    database[db['children']] = newtable2
    print(database[db['parents']])
    print(database[db['children']])

reading_file_to_dict(1)
reading_file_to_dict(2)
reading_file_to_dict(3)
print_children('Ivanov')
payment_status()
delete_info('Voronin')