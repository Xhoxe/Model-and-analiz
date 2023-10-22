def checkIfExist(arr):
    num_set = set(arr)
    if arr.count(0) > 1:
        return True
    num_set.discard(0)
    for num in arr:
        if 2 * num in num_set:
            return True          
        return False

print(checkIfExist([10,2,5,3]))
print(checkIfExist([3,1,7,11]))
