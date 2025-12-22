def mirrorDistance(n: int) -> int:
    num = n
    rev = 0
    while num>0:
        rev = rev*10 + num%10
        num//=10
    return abs(rev-n) 