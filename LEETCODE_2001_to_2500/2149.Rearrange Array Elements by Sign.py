def rearrangeArray(nums):
    p = [o for o in nums if o>0]
    n = [o for o in nums if o<0]
    v =[]
    for e,t in zip(p,n):
        v.append(e)
        v.append(t)
    return v