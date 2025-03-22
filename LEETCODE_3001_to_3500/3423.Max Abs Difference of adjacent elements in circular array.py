def maxAdjacentDistance(nums) -> int:
    nums.append(nums[0])
    maxDiff = 0
    for i in range(len(nums)-1):
        maxDiff = max(maxDiff,abs(nums[i]-nums[i+1]))
    return maxDiff  