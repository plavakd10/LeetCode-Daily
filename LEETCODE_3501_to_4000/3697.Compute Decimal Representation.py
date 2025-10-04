def decimalRepresentation(self, n: int):
    rev = str(n)[::-1]
    ans = []
    for i in range(len(rev)):
        a = int(rev[i])*10**i
        if a!=0:
            ans.append(a)
    return ans[::-1] 