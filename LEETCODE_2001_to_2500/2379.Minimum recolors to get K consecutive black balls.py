import math
def minimumRecolors(blocks: str, k: int) -> int:
    minW = math.inf
    for i in range(0,len(blocks)-k+1):
        w = blocks[i:i+k].count("W")
        minW = min(minW,w)
    return minW