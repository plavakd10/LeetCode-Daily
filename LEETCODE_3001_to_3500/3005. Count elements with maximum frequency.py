from collections import Counter
def maxFrequencyElements(nums) -> int:
    c  = Counter(nums)
    vals = list(c.values())
    return max(vals)*vals.count(max(vals))