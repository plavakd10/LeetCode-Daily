def generateKey(self, num1: int, num2: int, num3: int) -> int:
    val = [str(i).zfill(4) for i in (num1,num2,num3)]
    return int("".join(map(min,zip(*val))))