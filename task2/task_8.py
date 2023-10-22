def validMountainArray(arr):
    if len(arr) < 3:
        return False
    max_idx = arr.index(max(arr))
    if max_idx == 0 or max_idx == len(arr) - 1:
        return False
    for i in range(1, max_idx):
        if arr[i] <= arr[i - 1]:
            return False
    for i in range(max_idx + 1, len(arr)):
        if arr[i] >= arr[i - 1]:
            return False
    return True

print(validMountainArray([2, 1]))
print(validMountainArray([3, 5, 5]))
print(validMountainArray([0, 3, 2, 1]))
