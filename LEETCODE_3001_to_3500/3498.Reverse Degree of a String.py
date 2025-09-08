def reverseDegree(s: str) -> int:
    total = 0
    for i in range(len(s)):
        total += (i+1)*(123-ord(s[i]))
    return total 