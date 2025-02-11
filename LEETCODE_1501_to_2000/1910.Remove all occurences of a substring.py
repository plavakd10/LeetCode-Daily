def removeOccurrences(s,part) -> str:
    while part in s:
        s = s.replace(part,"",1)
    return s    
        