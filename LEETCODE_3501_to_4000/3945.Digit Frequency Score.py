from collections import Counter
def digitFrequencyScore(self, n: int) -> int:
    digits = [int(d) for d in str(n)]
    c = Counter(digits)
    total = 0
    for k,v in c.items():
        total += k*v
    return total    