from collections import Counter
def getLeastFrequentDigit(n: int) -> int:
    c = Counter(str(n))
    return int(sorted(c.items() , key = lambda x : (x[1], x[0]))[0][0])