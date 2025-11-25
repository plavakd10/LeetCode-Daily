def smallestRepunitDivByK(k) -> int:
    if k==1:
        return 1
    if k%2 == 0 or k % 5 == 0:
        return -1

    r = 0
    for i in range(1,k+1):
        r = (r*10+1)%k
    if r==0:
        return i
    return -1 