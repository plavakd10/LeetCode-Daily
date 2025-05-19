def smallestIndex(nums) -> int:
    def isindex(i,num):
        s = 0
        while num>0:
            s+=num%10
            num//=10
        return i==s
    for i in range(len(nums)):
        if isindex(i,nums[i]):
            return i
    return -1  