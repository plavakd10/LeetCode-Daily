def minQueenMoves(self, source: list[int], target: list[int]) -> int:
    a,b = source
    x,y = target
    return 0 if target == source else 1 if a==x or b==y or (a-x == b-y) or (a+b == x+y) else 2