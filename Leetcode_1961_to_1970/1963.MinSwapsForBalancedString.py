def minSwaps(s) -> int:
    max_close = 0
    ans = 0
    for i in s:
        if i==']':
            ans+=1
        else:
            ans-=1
        max_close = max(ans,max_close)
    return (max_close+1)//2            
        