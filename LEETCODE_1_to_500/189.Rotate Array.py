def rotate(nums,k) -> None:
    n = len(nums)
    k = k % n
    nums[:] = nums[n-k:] + nums[:n-k]