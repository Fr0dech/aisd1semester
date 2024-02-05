def quickSort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Берём опору
    left = [x for x in arr if x < pivot]  # Меньше опоры
    middle = [x for x in arr if x == pivot]  # Равно опоре
    right = [x for x in arr if x > pivot]  # Больше опоры

    # Сортируем микрочела
    return quickSort(left) + middle + quickSort(right)

arr = [170, 45, 75, 90, 802, 24, 2, 66]
print(quickSort(arr))
