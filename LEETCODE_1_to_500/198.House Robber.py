def rob(nums) -> int:
    prev2 = 0
    prev = nums[0]
    for i in range(1,len(nums)):
        take = nums[i]
        if i>1:
            take+=prev2
        notTake = prev

        curr = max(take,notTake)
        prev2 = prev
        prev = curr
    return prev 