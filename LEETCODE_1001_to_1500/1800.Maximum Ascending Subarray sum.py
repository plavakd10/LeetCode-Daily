def maxAscendingSum(nums) -> int:
    currSum = nums[0]
    ans = nums[0]
    for i in range(1,len(nums)):
        if nums[i]>nums[i-1]:
            currSum+=nums[i]
        else:
            currSum=nums[i]
        ans = max(ans,currSum)    
    return ans 