import math
def minElement(nums) -> int:
    res = math.inf
    for i in nums:
        c = 0
        while i:
            c+= i%10
            i//=10
        res = min(res,c)
    return res  