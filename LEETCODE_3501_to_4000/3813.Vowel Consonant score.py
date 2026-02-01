from math import floor
def vowelConsonantScore(s: str) -> int:
    vowels = "aeiou"
    v = c = 0
    for ch in s:
        if ch in vowels:
            v+=1
        elif ch.isalpha():
            c+=1
    if c>0:
        return floor(v/c)
    return 0