def minMergedInteger(self, nums: list[int]) -> int:
    arr = []
    for i in range(0,len(nums),2):
        n = int(str(nums[i]) + str(nums[i+1]))
        arr.append(n)
    return min(arr) 