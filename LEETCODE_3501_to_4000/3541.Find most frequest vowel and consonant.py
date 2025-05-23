from collections import defaultdict
def maxFreqSum(self, s: str) -> int:
    v = defaultdict(int)
    c = defaultdict(int)
    for st in s:
        if st in ['a','e','i','o','u']:
            v[st] +=1
        else:
            c[st] +=1
    max_val_vowels = max(v.values(), default=0) if v else 0
    max_val_cons = max(c.values(), default=0) if c else 0 
    return max_val_vowels+max_val_cons   