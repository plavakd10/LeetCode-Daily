def countKConstraintSubstrings(self, s: str, k: int) -> int:
    n = len(s)
    res = 0
    for i in range(n):
        count_zero, count_one = 0,0
        for j in range(i,n):
            if s[j]=='0':
                count_zero +=1
            else:
                count_one +=1
            if count_zero<=k or count_one<=k:
                res+=1
    return res 