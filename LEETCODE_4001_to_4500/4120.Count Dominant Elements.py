def countDominantElements(self, nums: list[int]) -> int:
    n = len(nums)
    dom = 0
    for i,x in enumerate(nums):
        nb_sum = 0
        count = 0
        if i>0:
            nb_sum+=nums[i-1]
            count+=1
        if i+1<n:
            nb_sum+=nums[i+1]
            count+=1
        if x*count >= nb_sum:
            dom+=1
    return dom