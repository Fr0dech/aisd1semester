# Создание хеш-таблицы для некоторого файла
# С наложением
import zlib

array = []
with open("file.txt", "r") as f:
    a = f.readline().replace("\n", "").split(" ")
    while a != [""]:
        array += a
        a = f.readline().replace("\n", "").split(" ")

la = len(array)
hesh_table = [None] * la * 2
for i in array:
    hesh = zlib.crc32(bytes(i, "UTF-8"))
    hesh_table[hesh % (2*la)] = [hesh, i]
result = open("output_13.txt", "w+")
for i in hesh_table:
    if i:
        result.write(f"{i[0]} {i[1]}\n")
        print(*i)
result.close()
