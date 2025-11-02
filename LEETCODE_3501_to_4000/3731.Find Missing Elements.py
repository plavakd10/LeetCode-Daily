def findMissingElements(nums):
    mini = min(nums)
    maxi = max(nums)
    s = set(range(mini,maxi+1))
    nums.sort()
    ans = []
    for num in s:
        if num not in nums:
            ans.append(num)
    return sorted(ans)        
        