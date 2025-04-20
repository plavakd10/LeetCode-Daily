from collections import Counter
from math import ceil
def numRabbits(self, answers: List[int]) -> int:
    c = Counter(answers)
    ans = 0
    for k,v in c.items():
        gs = k+1
        g = ceil(v/gs)
        ans += g*gs
    return ans   