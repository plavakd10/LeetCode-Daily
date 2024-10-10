def maxWidthRamp(nums) -> int:
    right = [0]*len(nums)
    i = len(nums)-1
    prev_max = 0

    for n in reversed(nums):
        right[i] = max(n,prev_max)
        prev_max = right[i]
        i-=1
    i = 0
    ans = 0
    for r in range(len(nums)):
        while nums[i]>right[r]:
            i+=1
        ans = max(ans,r-i)
    return ans   