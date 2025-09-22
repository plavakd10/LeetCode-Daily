def evenNumberBitwiseORs(nums) -> int:
    ans = 0
    for i in nums:
        if i%2==0:
            ans = ans | i
    return ans  