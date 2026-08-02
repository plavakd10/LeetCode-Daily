def minimumSwaps(self, nums: list[int]) -> int:
    z = nums.count(0)
    n = len(nums)
    swaps = 0
    for i in range(n-1,n-z-1,-1):
        if nums[i]!=0:
            swaps+=1
    return swaps   