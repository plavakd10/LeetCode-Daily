def makeFancyString(s: str) -> str:
    temp = []
    for c in s:
        if len(temp)>=2 and temp[-1] == c and temp[-2] == c:
            continue
        temp.append(c)
    return ''.join(temp)        
            