def maxSum(nums) -> int:
    s = set(nums)
    ans = 0
    l = 0
    for item in s:
        if item>0:
            ans+=item
            l+=1
    if l==0:
        return max(s)
    return ans