def isMiddleElementUnique(self, nums: list[int]) -> bool:
    middle = nums[len(nums)//2]
    return nums.count(middle) == 1