from collections import Counter

def minimumLength(s: str) -> int:
    return sum(2 if val%2 == 0 else 1 for val in Counter(s).values())