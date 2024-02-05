def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Левачок больше корня? Заменяем...
    if left < n and arr[i] < arr[left]:
        largest = left

    # Правачок больше корня? Заменяем...
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Биг бой не корень?
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Заменяем...

        # Меняем дерево...
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    # Засобачил корень
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Воруем элементы из кучи
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Заменяем... Корень и последний элемент
        heapify(arr, i, 0)

    return arr

arr = [170, 45, 75, 90, 802, 24, 2, 66]
heapSort(arr)
print(arr)