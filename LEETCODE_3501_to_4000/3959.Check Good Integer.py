def checkGoodInteger(self, n: int) -> bool:
    num = n
    s1 = s2 = 0
    while num>0:
        dig = num%10
        s1+=dig
        s2+=dig*dig
        num//=10
    return s2-s1>=50 