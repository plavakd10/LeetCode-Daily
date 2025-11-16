from collections import defaultdict
def numSub(s: str) -> int:
    d = defaultdict(int)
    c = 0
    for char in s:
        if char == "1":
            c+=1
        else:
            if c>0:
                d[c] = d.get(c,0) + 1
            c = 0
    if c>0:
        d[c] = d.get(c,0) + 1
    ans = 0 
    for k,v in d.items():
        ans += (v*k*(k+1)//2)%(10**9+7)
    return ans 