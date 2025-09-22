def maxKDistinct(nums,k):
    s = sorted(set(nums))
    return s[-k:][::-1]