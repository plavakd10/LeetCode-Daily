def missingMultiple(nums, k: int) -> int:
    for i in range(k,1000,k):
        if i not in nums: 
            return i
                

        