pow = [0, 1, 10, 100, 1000, 10000, 100000]
def largestInteger(self, n: int, s: int) -> int:
    if s > n * 9: return -1
    q, r = divmod(s, 9)

    return self.pow[n + 1] - self.pow[n - q + 1] + r * self.pow[n - q] 