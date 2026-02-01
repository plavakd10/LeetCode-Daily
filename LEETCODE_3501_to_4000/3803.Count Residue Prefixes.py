def residuePrefixes(s: str) -> int:
    def dist(a):
        return len(set(a))
    count = 0
    for r in range(1,len(s)+1):
        if dist(s[0:r]) == len(s[0:r])%3:
            count+=1
    return count  