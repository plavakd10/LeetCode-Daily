def countOppositeParity(self, nums: list[int]) -> list[int]:
    n = len(nums)
    e,o = 0,0
    ans = [0]*n

    for i in range(n-1,-1,-1):
        if nums[i]%2==1:
            ans[i] = e
            o+=1
        else:
            ans[i] = o
            e +=1
    return ans