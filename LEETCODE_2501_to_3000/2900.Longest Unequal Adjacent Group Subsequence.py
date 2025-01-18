def getLongestSubsequence(words,groups):
    ans = []
    t = -1
    n = len(groups)
    for i in range(n):
        if (groups[i]!=t):
            t = groups[i]
            ans.append(words[i])
    return ans    