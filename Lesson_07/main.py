from export_import import print_horizontal, print_vertical, import_data, data_input 
from logger import dict_read, dict_write
from dictionary import d

def dict_ui():
    print('Hi! Welcome to our dictionary')
    first = input('If you want to read it, type 1,\n if you want to write data in, type 2: ')
    if first == '1':
        read_v = input('Horizontal or vertical view? ')
        if read_v.lower() == 'horizontal':
            print_horizontal(d)
        if read_v.lower() == 'vertical':
            print_vertical(d)
    if first == '2':
        import_data(d, data_input())
        dict_write()
        dict_read()







