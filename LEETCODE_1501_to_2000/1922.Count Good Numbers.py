def countGoodNumbers(self, n: int) -> int:
    mod = 10**9+7
    e = (n+1)//2
    o = n//2
    return (pow(5,e,mod)*pow(4,o,mod))%mod
        