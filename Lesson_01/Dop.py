n = int(input('Enter n: '))
one = 1
two = 1
for i in range(1, n - 1):
    (one, two) = (two, one + two)
print(two)
