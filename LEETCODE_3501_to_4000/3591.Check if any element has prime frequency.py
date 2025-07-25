from collections import Counter
def checkPrimeFrequency(nums) -> bool:
    def isPrime(n):
        if n<=1:
            return False
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
    c = Counter(nums)
    for v in c.values():
        if isPrime(v):
            return True
    return False                        
        