def makeEqual(words) -> bool:
    c = {}
    for word in words:
        for letter in word:
            c[letter] = c.get(letter,0)+1
    for l in c.values():
        if l%len(words)!=0:
            return False
    return True 