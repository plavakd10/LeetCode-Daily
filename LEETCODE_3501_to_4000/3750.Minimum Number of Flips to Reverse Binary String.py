def minimumFlips(n: int) -> int:
    ib = int(bin(n)[2:][::-1],2)
    return bin(n ^ ib)[2:].count("1")