from collections import deque


def task7(nums, k):
    if not nums:
        return []
    if k == 1:
        return nums
    deq = deque()
    max_nums = []
    for i, num in enumerate(nums):
        while deq and deq[0] < i - k + 1:
            deq.popleft()
        while deq and nums[deq[-1]] < num:
            deq.pop()
        deq.append(i)
        if i >= k - 1:
            max_nums.append(nums[deq[0]])
    
    return max_nums

print(task7([1,3,-1,-3,5,3,6,7], 3)) 
print(task7([1], 1))
