def prefixCount(words, pref: str) -> int:
    ans = 0
    for word in words:
        ans+= word.startswith(pref)
    return ans 