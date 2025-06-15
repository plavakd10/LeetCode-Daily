import math
def maxProduct(nums) -> int:
    pre,suf = 1,1
    ans = -math.inf
    for i in range(len(nums)):
        if pre == 0:
            pre = 1
        if suf == 0:    
            suf = 1
        pre*=nums[i]
        suf*=nums[len(nums)-i-1]
        ans = max(ans, max(pre,suf))
    return ans  