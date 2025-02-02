def check(nums) -> bool:
    n = len(nums)
    cnt = 0
    for i in range(n):
        if nums[i]>nums[(i+1)%n]:
            cnt+=1
        if cnt>1:
            return False
    return True   