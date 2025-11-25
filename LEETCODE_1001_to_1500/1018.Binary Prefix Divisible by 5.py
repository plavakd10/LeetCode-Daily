def prefixesDivBy5(nums):
    ans = []
    curr = 0
    for n in nums:
        curr = (curr << 1)+n
        ans.append(curr%5==0)
    return ans 