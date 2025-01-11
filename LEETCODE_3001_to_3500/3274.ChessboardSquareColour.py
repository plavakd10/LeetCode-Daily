def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
    isSame = lambda x: (ord(x[0]) + int(x[1]))%2==0
    return isSame(coordinate1)==isSame(coordinate2)  