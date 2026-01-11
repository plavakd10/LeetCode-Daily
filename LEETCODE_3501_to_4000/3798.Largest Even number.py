def largestEven(s: str) -> str:
    if int(s[-1])%2==0:
        return s
    i = len(s)-1
    while i>=0:
        if int(s[i])%2!=0:
            i-=1
        else:
            return s[:i+1] 
    return ""