# Создание хеш-таблицы для некоторого файла
# Со списками
import zlib

array = []
with open("file.txt", "r") as f:
    a = f.readline().replace("\n", "").split(" ")
    while a != [""]:
        array += a
        a = f.readline().replace("\n", "").split(" ")

la = len(array)
hesh_table = [None] * la
for i in array:
    hesh = zlib.crc32(bytes(i, "UTF-8"))
    if hesh_table[hesh % la]:
        hesh_table[hesh % la].append([hesh, i])
    else:
        hesh_table[hesh % la] = [[hesh, i]]
result = open("output_14.txt", "w+")
for i in hesh_table:
    if i:
        for j in i:
            result.write(f"{j[0]} {j[1]} ")
            print(*j, end=" ")
        print()
        result.write("\n")
result.close()
