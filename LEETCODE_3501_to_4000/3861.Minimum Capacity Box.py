import math
def minimumIndex(capacity: list[int], itemSize: int) -> int:
    ans, idx = math.inf, -1
    for i, c in enumerate(capacity):
        if itemSize <= c < ans:
            ans, idx = c, i
    return idx      