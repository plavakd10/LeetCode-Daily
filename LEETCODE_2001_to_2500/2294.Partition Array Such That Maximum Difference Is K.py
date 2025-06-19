def partitionArray(nums, k: int) -> int:
    nums.sort()
    count = 1
    mini = nums[0]
    for i in range(1,len(nums)):
        if nums[i] - mini > k:
            mini = nums[i]
            count+=1
    return count  