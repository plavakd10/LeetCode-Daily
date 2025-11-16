def findDisappearedNumbers(nums):
    for num in nums:
        index = abs(num)-1
        nums[index] = -abs(nums[index])
    ans = []
    for i,v in enumerate(nums):
        if v>0:
            ans.append(i+1)
    return ans  