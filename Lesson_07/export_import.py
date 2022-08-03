from dictionary import d


def print_vertical(d):
    for i in range(len(d)):
        print(*d[i], sep='\n')

def print_horizontal(d):
    print(d)

def data_input():
    data = input('Write throung comma - new name, phone and city: ').split(',')
    return data

def import_data(d, function):

    d[len(d)] = function[0], function[1], function[2]
    return d
