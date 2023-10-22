def removeDuplicates(nums):
    if not nums:
        return 0
    insert_pos = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[insert_pos] = nums[i]
            insert_pos += 1   
            return insert_pos

nums1 = [1, 1, 2]
print(removeDuplicates(nums1), nums1)

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(nums2))
