def findFinalValue(nums, original: int) -> int:
    seen=set(nums)
    x=original
    while x<=1000:
        if x in seen: x*=2
        else: break
    return x 