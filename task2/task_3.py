def sortedSquares(nums):
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    pos = n - 1
    
    while left <= right:
        left_sq = nums[left] ** 2
        right_sq = nums[right] ** 2
        
        if left_sq > right_sq:
            result[pos] = left_sq
            left += 1
        else:
            result[pos] = right_sq
            right -= 1      
        pos -= 1 
    return result

print(sortedSquares([-4, -1, 0, 3, 10]))
print(sortedSquares([-7, -3, 2, 3, 11]))
