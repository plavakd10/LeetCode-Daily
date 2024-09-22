def lengthOfLongestSubstring(s: str) -> int:
    l = 0
    res = 0
    set1 = set()

    for r in range(len(s)):
        while(s[r] in set1):
            set1.remove(s[l])
            l+=1
        set1.add(s[r])
        res = max(res,r-l+1)
    return res

input1 = "abcabcbb"
input2 = "bbbbb"
input3 = "pwwkew"

print(lengthOfLongestSubstring(input1))
print(lengthOfLongestSubstring(input2))
print(lengthOfLongestSubstring(input3))