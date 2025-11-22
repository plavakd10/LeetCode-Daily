def minimumOperations(nums) -> int:
    ans = 0
    for i in nums:
        if i%3!=0:
            ans+=1
    return ans