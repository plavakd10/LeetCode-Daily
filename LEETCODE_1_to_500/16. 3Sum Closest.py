import math
def threeSumClosest(nums, target: int) -> int:
    nums.sort()
    closest = math.inf
    mini = math.inf

    for i in range(len(nums)-2):
        l,r = i+1, len(nums)-1

        while l < r:
            currsum = nums[i] + nums[l] + nums[r]
            currdiff = abs(currsum - target)

            if currdiff < mini:
                mini = currdiff
                closest = currsum

            if currsum < target:
                l+=1
            else:
                r-=1
    return closest 