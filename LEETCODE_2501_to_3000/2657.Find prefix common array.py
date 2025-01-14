def findThePrefixCommonArray(A,B):
    ans = []
    n = len(A)
    common = 0
    seen = [0]*(n+1)
    for i in range(n):
        if seen[A[i]] == 0:
            seen[A[i]] = 1
        elif seen[A[i]] == 1:
            common +=1   
        if seen[B[i]] == 0:
            seen[B[i]] = 1
        elif seen[B[i]] == 1:
            common+=1
        ans.append(common)
    return ans  