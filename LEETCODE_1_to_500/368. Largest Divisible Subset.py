def largestDivisibleSubset(nums):
    nums.sort()
    dp = [[num] for num in nums]
    ans = []

    for i in reversed(range(len(nums))):
        for j in range(i+1,len(nums)):
            if nums[j]%nums[i]==0:
                temp = [nums[i]]+dp[j]
                dp[i] = temp if len(temp) > len(dp[i]) else dp[i]
        ans = dp[i] if len(dp[i])  > len(ans) else ans
    return ans  