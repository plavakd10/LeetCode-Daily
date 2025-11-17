def kLengthApart(nums, k: int) -> bool:
    if k == 0:
        return True
    prev = None
    for i,v in enumerate(nums):
        if v==1:
            if prev is not None and i-prev<=k:
                return False
            prev = i
    return True 