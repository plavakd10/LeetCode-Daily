from collections import Counter
def rearrangeArray(self, nums: list[int]) -> list[int]:
    f, ans = Counter(nums), []
    while f:
        ans += sorted(f)
        f -= Counter(f.keys())
    return ans