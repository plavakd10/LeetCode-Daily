def findMissingAndRepeatedValues(grid):
    arr = []
    for i in grid:
        arr.extend(i)
    s = set(arr)
    s1 = set(range(1,len(arr)+1))    
    ans = [0,list(s1.difference(s))[0]]
        
    seen = {}
    for i in arr:
        if i in seen:
            ans[0]=i
            break
        else:
            seen[i]=1
    return ans            