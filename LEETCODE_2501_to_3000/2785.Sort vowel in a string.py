def sortVowels(self, s: str) -> str:
    s = list(s)
    vowels = []
    for i in range(len(s)):
        if s[i] in 'aeiouAEIOU':
            vowels.append(s[i])
            s[i] = -1
    vowels  = sorted(vowels)[::-1]
    for i in range(len(s)):
        if s[i] == -1:
            s[i] = vowels.pop()
    return "".join(s) 