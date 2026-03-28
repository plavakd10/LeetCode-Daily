from collections import Counter
def firstUniqueEven(self, nums: list[int]) -> int:
    c = Counter(nums)
    for n in nums:
        if n%2==0 and c[n]==1:
            return n
    return -1   