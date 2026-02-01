def minimumCost(nums) -> int:
    n = nums[1:]
    n.sort()
    return nums[0]+n[0]+n[1]