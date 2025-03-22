def subarraySum(nums) -> int:
    ts = 0
    for i in range(len(nums)):
        start = max(0,i-nums[i])
        ts+= sum(nums[start:i+1])
    return ts   