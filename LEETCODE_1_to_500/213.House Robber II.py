def maxSum(arr):
    prev2 = 0
    prev = arr[0]
    for i in range(1,len(arr)):
        take = arr[i]
        if i>1:
            take+=prev2
        nonTake = prev

        curr = max(take,nonTake)
        prev2 = prev
        prev = curr
    return prev    
def rob(nums) -> int:
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    return max(maxSum(nums[1:]),maxSum(nums[:-1]))    
