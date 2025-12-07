def sortByReflection(nums):
    def reflect(x: int) -> int:
        rev = 0
        while x > 0:
            rev = (rev << 1) | (x & 1)
            x >>= 1                   
        return rev
    nums.sort(key=lambda x: (reflect(x), x))
    return nums