def sortArrayByParity(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        while left < right and nums[left] % 2 == 0:
            left += 1
        while left < right and nums[right] % 2 == 1:
            right -= 1
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
    return nums

print(sortArrayByParity([3, 1, 2, 4]))
print(sortArrayByParity([0]))
