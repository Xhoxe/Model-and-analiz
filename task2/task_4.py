def duplicateZeros(arr):
    zeros = arr.count(0)
    if zeros == 0:
        return
    length = len(arr) + zeros
    i = len(arr) - 1
    j = length - 1
    
    while i < j:
        if arr[i] != 0:
            if j < len(arr):
                arr[j] = arr[i]
            j -= 1
        else:
            if j < len(arr):
                arr[j] = arr[i]
            j -= 1
            if j < len(arr):
                arr[j] = arr[i]
            j -= 1
        i -= 1

arr1 = [1, 0, 2, 3, 0, 4, 5, 0]
duplicateZeros(arr1)
print(arr1)

arr2 = [1, 2, 3]
duplicateZeros(arr2)
print(arr2)
