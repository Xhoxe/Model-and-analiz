def replaceElements(arr):
    maxRight = -1
    for i in range(len(arr) - 1, -1, -1):
        current = arr[i]
        arr[i] = maxRight
        maxRight = max(maxRight, current)
    return arr

print(replaceElements([17, 18, 5, 4, 6, 1]))
print(replaceElements([400]))
