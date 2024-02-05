def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    # Делим делимое
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Делим делимое делёное
    left_half = mergeSort(left_half)
    right_half = mergeSort(right_half)

    # Объединяем делёное
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index = right_index = 0

    # Добавляем в итоговый массив наименьшее
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Закидываем остатки слева
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    # Закидываем остатки справа
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

arr = [170, 45, 75, 90, 802, 24, 2, 66]
print(mergeSort(arr))