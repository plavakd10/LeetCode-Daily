def scoreBalance(s: str) -> bool:
    score = 0 
    prefix = 0
    for c in s:
        score += ord(c)-ord('a')+1
    for c in s:
        prefix += ord(c)-ord('a')+1
        if 2*prefix == score:
            return True
    return False