def maxArea(height) -> int:
    ans = 0
    l,r = 0, len(height)-1
    while l<=r:
        m = min(height[l],height[r])
        d = r-l
        md = d*m
        ans = max(ans,md)
        if height[l]<=height[r]:
            l+=1
        else:
            r-=1
    return ans 