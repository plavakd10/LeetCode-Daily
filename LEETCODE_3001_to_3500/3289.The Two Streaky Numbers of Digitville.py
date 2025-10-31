from collections import defaultdict
def getSneakyNumbers(nums):
    d = defaultdict(int)
    ans = []
    for num in nums:
        d[num] = d.get(num,0) + 1
        if d[num] == 2:
            ans.append(num)
    return ans