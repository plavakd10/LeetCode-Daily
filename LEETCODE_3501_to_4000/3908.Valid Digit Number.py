def validDigit(self, n: int, x: int) -> bool:
    return not str(n).startswith(str(x)) and str(n).count(str(x))>0