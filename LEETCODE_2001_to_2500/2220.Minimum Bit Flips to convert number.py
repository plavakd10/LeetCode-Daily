def minBitFlips(self, start: int, goal: int) -> int:
    count = 0 
    n = start ^ goal
    while n!=0:
        n = n & (n-1)
        count+=1
    return count    