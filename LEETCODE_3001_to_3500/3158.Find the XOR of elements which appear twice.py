from collections import Counter
from functools import reduce
from operator import xor
def duplicateNumbersXOR(nums) -> int:
    c = Counter(nums)
    res = []
    for k,v in c.items():
        if v==2:
            res.append(k)
    if len(res)==0:
        return 0
    return reduce(xor,res)            