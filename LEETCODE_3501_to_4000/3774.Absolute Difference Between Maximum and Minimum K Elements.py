def absDifference(nums, k: int) -> int:
    nums.sort()
    n = len(nums)
    return abs(sum(nums[:k])-sum(nums[n-k:]))