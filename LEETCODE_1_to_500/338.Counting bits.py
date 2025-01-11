def countBits(n: int):
    return [i.bit_count() for i in range(n+1)] 