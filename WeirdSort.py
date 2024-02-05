def merge_sort(input_file, output_file, buffer_size):
    # Чтение исходного файла
    with open(input_file, 'r') as file:
        data = file.readlines()
        data = list(map(int, data))
        print(data)

    # Сортировка и запись куска в файл
    def sort_and_write(chunk):
        chunk.sort()
        with open(output_file, 'a') as file:
            file.writelines(str(chunk))

    # Разделение данных на куски и рекурсия
    chunks = [data[i:i + buffer_size] for i in range(0, len(data), buffer_size)]
    for chunk in chunks:
        sort_and_write(chunk)

    # Мерджирование кусков и запись
    while len(chunks) > 1:
        next_chunks = []
        for i in range(0, len(chunks), 2):
            if i + 1 < len(chunks):
                # Объединение двух отсортированных кусков
                merged_chunk = []
                chunk1 = chunks[i]
                chunk2 = chunks[i + 1]
                index1, index2 = 0, 0

                while index1 < len(chunk1) and index2 < len(chunk2):
                    if chunk1[index1] < chunk2[index2]:
                        merged_chunk.append(chunk1[index1])
                        index1 += 1
                    else:
                        merged_chunk.append(chunk2[index2])
                        index2 += 1

                merged_chunk.extend(chunk1[index1:])
                merged_chunk.extend(chunk2[index2:])

                # Запись объединенного куска в файл
                sort_and_write(merged_chunk)
                next_chunks.append(merged_chunk)
            else:
                # Случай с нечётным куском
                next_chunks.append(chunks[i])

        chunks = next_chunks

    # Запись аутпута
    with open(output_file, 'w') as file:
        file.writelines(str(chunks[0]))



input_file = 'input.txt'
output_file = 'output.txt'
buffer_size = 3  # Размер буфера для сортировки

merge_sort(input_file, output_file, buffer_size)