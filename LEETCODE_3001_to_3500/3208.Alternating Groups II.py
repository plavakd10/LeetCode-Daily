def numberOfAlternatingGroups(colors, k: int) -> int:
    n = len(colors)
    ans = 0
    left = 0
    for right in range(1,n+k-1):
        if colors[right%n] == colors[(right-1)%n]:
            left = right
        if right-left+1>k:
            left+=1
        if right-left+1==k:
            ans+=1
    return ans