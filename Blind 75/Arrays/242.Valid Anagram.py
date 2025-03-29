from collections import defaultdict
def isAnagram(s: str, t: str) -> bool:
    counter = defaultdict(int)
    for num in s:
        counter[num]+=1
    for num in t:
        counter[num]-=1
    for v in counter.values():
        if v!=0:
            return False
    return True