def task8(nums, k):
    n = len(nums)
    dp = [-float('inf')] * n
    dp[0] = nums[0]

    for i in range(1, n):
        for j in range(max(0, i - k), i):
            dp[i] = max(dp[i], dp[j] + nums[i])

    return max(dp)

print(task8([10,2,-10,5,20], 2)) 
print(task8([-1,-2,-3], 1)) 
print(task8([10,-2,-10,-5,20], 2))
