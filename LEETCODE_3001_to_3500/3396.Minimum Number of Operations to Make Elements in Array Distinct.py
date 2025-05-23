def minimumOperations(nums) -> int:
    count=0
    while len(nums)>len(set(nums)):
        nums=nums[3:]
        count+=1
    return count
