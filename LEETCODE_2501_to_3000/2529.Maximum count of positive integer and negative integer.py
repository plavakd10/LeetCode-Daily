def maximumCount(nums) -> int:
    ans = 0
    pos,neg = 0,0
    for num in nums:
        if num>0:
            pos+=1
        elif num<0:
            neg+=1
        ans = max(pos,neg)
    return ans