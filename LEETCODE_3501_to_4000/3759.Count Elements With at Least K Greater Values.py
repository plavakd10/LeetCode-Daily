def countElements(nums, k: int) -> int:
    if k==0:
        return len(nums)
    nums.sort()
    n = len(nums)

    t = nums[n-k]
    ans = 0 
    for i in nums:
        if i<t:
            ans+=1
    return ans 