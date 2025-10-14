def hasIncreasingSubarrays(nums, k: int) -> bool:
    def increasing(arr):
        for i in range(len(arr)-1):
            if arr[i]>=arr[i+1]:
                return False
        return True         

    l = len(nums)
    start = l - 2*k
    while start>=0:
        arr1 = nums[start:start+k]
        arr2 = nums[start+k:start+(2*k)]
        if increasing(arr1) and increasing(arr2):
            return True
        start-=1
    return False