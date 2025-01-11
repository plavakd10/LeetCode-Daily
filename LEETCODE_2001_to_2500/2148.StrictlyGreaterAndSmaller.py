def countElements(nums) -> int:
    a,b = min(nums), max(nums)
    ans = 0
    for i in nums:
        if i>a and i<b:
            ans+=1
    return ans     