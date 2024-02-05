unsorted = []
sorted = []
temporal = 0
unsorted = input().split()
for i in range(len(unsorted)):
    unsorted[i] = int(unsorted[i])
print(unsorted)
sorted = unsorted
for i in range(1, len(unsorted)):
    temp = unsorted[i]
    j = i - 1
    while (temp < unsorted[j] and j >= 0):
        sorted[j + 1] = unsorted[j]
        j = j - 1
    unsorted[j + 1] = temp

print(sorted)
