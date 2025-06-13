from collections import Counter
def maxDifference(s: str) -> int:
    c = Counter(s)
    v1 = []
    for k,v in c.items():
        v1.append(v)
    v1.sort()
    mini = 0
    maxi = 0
    for i in range(len(v1)):
        if v1[i]%2==0:
            mini = v1[i]
            break
    for i in range(len(v1)-1,-1,-1):
        if v1[i]%2!=0:
            maxi = v1[i]
            break
    return maxi-mini