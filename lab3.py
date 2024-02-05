numba = int(input('Введите число '))
thre = 0
fiv = 0
sevn = 0
counter = 0

for i in range(1, numba + 1, 2):
    initi = i
    if (i % 3) == 0:
        while (i % 3) == 0:
            i = i // 3
            thre += 1
    if (i % 5) == 0:
        while (i % 5) == 0:
            i = i // 5
            fiv += 1
    if (i % 7) == 0:
        while (i % 7) == 0:
            i = i // 7
            sevn += 1
    if i == 1:
        print(initi, ' = ', ' 3^', thre, ' 5^', fiv, ' 7^', sevn, sep='')
        counter += 1

    thre = 0
    fiv = 0
    sevn = 0
    initi = 0
print(counter)