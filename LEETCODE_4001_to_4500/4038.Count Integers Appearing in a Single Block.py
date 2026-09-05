def countSpecialIntegers(self, nums: list[int]) -> int:
    d = {}
    n = len(nums)
    d[nums[0]] = 1
    for i in range(1,n):
        if nums[i] != nums[i-1]:
            d[nums[i]] = d.get(nums[i],0)+1
    count = 0
    for v in d.values():
        if v == 1:
            count+=1
    return count  