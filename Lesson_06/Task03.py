# Напишите функцию, которая проверит стихи на ритм. 

def vowels_in_string(line):
    value = list()
    for i in line:
        value.append(sum(True for j in i if j in 'аяоёуюэеыиАЯОУЮЭЕИ'))
    if value.count(value[0]) == len(value):
        return 'Парам пам-пам'
    return 'Пам парам'

song = input('Write your song: ').split(' ')
print(vowels_in_string(song))
