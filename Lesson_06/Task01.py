# Напишите такое лямбда выражение transformation, чтобы transformed_values 
# получился копией values

values = [2, 3, 5, 6, 8, 9, 3, 4, 'hi', 7]
global transformation 
transformation = lambda x: x*1
transformed_values = list(map(transformation, values))

if values == transformed_values:
    print('ok')
else:
    print('not ok')