def countPrimes(n):
    if n<=2:
        return 0
    primes = [True]*n
    primes[0] = primes[1] = False
    count = 0
    for i in range(2,n):
        if primes[i]:
            count+=1
            for j in range(i*i,n,i):
                primes[j] = False
    return count            