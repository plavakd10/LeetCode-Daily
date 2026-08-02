def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
    i = 0
    for n in nums:
        if i<k or n!=nums[i-k]:
            nums[i] = n
            i+=1
    while len(nums) > i:
        nums.pop()
    return nums