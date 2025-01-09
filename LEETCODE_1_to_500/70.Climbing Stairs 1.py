def climbStairs(n) -> int:
    if n<=2:
        return n
    a,b,c=1,1,0
    for i in range(n-1):
        c=a+b
        b=a
        a=c
    return c  