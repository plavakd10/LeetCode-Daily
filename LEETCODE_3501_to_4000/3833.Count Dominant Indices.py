def dominantIndices(nums) -> int:
    avg_arr = []
    n = len(nums)
    s = 0
    c = 0
    for i in range(n-1,-1,-1):
        s+=nums[i]
        c+=1
        avg_arr.append(s/c)
    ans = 0
    for i in range(n-1):
        if nums[i]>avg_arr[::-1][i+1]:
            ans+=1
    return ans 