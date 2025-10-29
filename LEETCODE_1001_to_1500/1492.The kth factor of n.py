def kthFactor(n: int, k: int) -> int:
    factt = [1]
    for i in range(2,(n//2)+1):
        if n%i==0:
            factt.append(i)
    factt.append(n)        
    return -1 if k>len(factt) else factt[k-1]