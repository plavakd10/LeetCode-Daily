def sumOfGoodNumbers(nums, k: int) -> int:
    s = 0
    for i,num in enumerate(nums):
        if i-k>=0 and num<=nums[i-k]:
            continue
        if i+k<len(nums) and num<=nums[i+k]:
            continue
        s+=num
    return s  