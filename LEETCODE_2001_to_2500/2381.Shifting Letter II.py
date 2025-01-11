def shiftingLetters(s: str, shifts) -> str:
    prefix = [0]*(len(s)+1)
    for l,r,d in shifts:
        prefix[r+1] +=1 if d else -1
        prefix[l] +=-1 if d else 1

    difference = 0
    res = [ord(ch)-ord("a") for ch in s]

    for i in reversed(range(len(prefix))):
        difference+=prefix[i]

        res[i-1] = (difference + res[i-1] + 26)%26
    s = [chr(ord("a")+n) for n in res]
    return "".join(s)   