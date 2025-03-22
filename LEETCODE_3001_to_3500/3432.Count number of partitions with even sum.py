def countPartitions(nums) -> int:
    if sum(nums)%2==0:
        return len(nums)-1
    return 0  