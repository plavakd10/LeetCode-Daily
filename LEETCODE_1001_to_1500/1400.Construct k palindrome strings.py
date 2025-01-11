from collections import Counter
def canConstruct(s: str, k: int) -> bool:
    c = Counter(s)
    if len(s)<k:
        return False
    odd_num = 0    
    for i in c.values():
        odd_num += i%2
    return odd_num<=k