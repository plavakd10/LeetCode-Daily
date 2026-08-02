def maxDigitRange(self, nums: list[int]) -> int:
    def ranger(num):
        if num == 0:
            return 0
        mx = 0
        mn = 9
        while num > 0:
            digit = num % 10
            mx = max(mx, digit)
            mn = min(mn, digit)
            num //= 10
        return mx - mn    
    
    maxDigitRange = -1
    for n in nums:
        maxDigitRange = max(maxDigitRange, ranger(n))
    ans = 0
    for n in nums:
        if ranger(n) == maxDigitRange:
            ans+=n
    return ans