def maximumSum(nums) -> int:
    def digitSum(n):
        s = 0
        while (n>0):
            s+= n%10
            n//=10
        return int(s)
    maxSum = -1
    d = {}
    for i in range(len(nums)):
        ds = digitSum(nums[i])
        if ds not in d:
            d[ds] = nums[i]
        else:
            maxSum = max(maxSum,nums[i]+d[ds])          
            d[ds] = max(d[ds],nums[i])
    return maxSum    