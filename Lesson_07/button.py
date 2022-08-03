from export_import import print_horizontal, print_vertical, import_data, data_input 
from logger import dict_read, dict_write
from dictionary import d
from main import dict_ui

while True:
    dict_ui()
    contin = input('If you want to continue press 1')
    if contin != '1':
        break  
        