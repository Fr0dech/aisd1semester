negr = []
negr = input().split()
for i in range(len(negr)):
    negr[i] = int(negr[i])

n = len(negr)
gap = n // 2

while gap > 0:
    for i in range(gap, n):
        temp = negr[i]
        j = i
        while j >= gap and negr[j - gap] > temp:
            negr[j] = negr[j - gap]
            j -= gap
        negr[j] = temp
    gap //= 2

print(negr)