# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

print('x, y, z')
result = True
for x in range(2):
    for y in range(2):
        for z in range(2):
            print(x, y, z, end=' - ')
            if not(x and y and z) == (not x or not y or not z):
                print('yes')
            else:
                result = False
        
print(f'Result verification is {result}')
