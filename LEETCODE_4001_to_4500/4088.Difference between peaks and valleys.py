def peakValleyDifference(self, nums: list[int]) -> int:
    n = len(nums)
    peak_sum = sum([nums[i] for i in range(1,n-1) if nums[i-1]<nums[i]>nums[i+1]])
    valley_sum = sum([nums[i] for i in range(1,n-1) if nums[i-1]>nums[i]<nums[i+1]])
    return peak_sum-valley_sum