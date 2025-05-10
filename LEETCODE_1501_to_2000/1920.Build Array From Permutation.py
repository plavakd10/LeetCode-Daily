def buildArray(nums):
    ans = [0] * len(nums)
    for i in range(len(nums)):
        ans[i] = nums[nums[i]]
    return ans   
        