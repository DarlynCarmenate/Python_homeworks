# Напишите функцию print_operation_table(operation, num_rows, num_columns), 
# которая принимает в качесте аргумента лямбда функцию и высчитывает таблицу умножения,
# сложения или возвредения в степень

def print_operation_table(operation, num_rows=9, num_columns=9):
    a = list()
    a = [operation(i, j) for i in range(1, num_rows + 1) for j in range(1, num_columns + 1)]
    k=0
    for i in a:
        print(i, end=' \t')
        k+=1
        if k == num_columns:
            print()
            k=0

print_operation_table(lambda i, j: i * j)
