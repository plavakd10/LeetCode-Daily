def maximizeExpressionOfThree(nums) -> int:
    nums.sort()
    return nums[-1]+nums[-2]-nums[0]