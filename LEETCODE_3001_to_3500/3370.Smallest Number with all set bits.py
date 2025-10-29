def smallestNumber(n: int) -> int:
    l = len(bin(n)[2:])
    return 2**l - 1