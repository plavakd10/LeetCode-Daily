from collections import Counter
def sumDivisibleByK(nums,k: int) -> int:
    s = 0
    c = Counter(nums)
    for ke,v in c.items():
        if v%k==0:
            s+=v*ke
    return s  