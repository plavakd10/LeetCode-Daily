def maximumDifference(nums) -> int:
    ans = -1
    pre = nums[0]
    for i in range(1,len(nums)):
        if nums[i] > pre:
            ans = max(ans,nums[i]-pre)
        else:
            pre = nums[i]
    return ans 