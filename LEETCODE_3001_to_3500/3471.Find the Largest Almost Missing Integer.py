from collections import defaultdict
def largestInteger(nums, k: int) -> int:
    d = defaultdict(int)
    n = len(nums)

    for i in range(n-k+1):
        for num in set(nums[i:i+k]):
            d[num] = d.get(num,0) + 1
    ans = -1
    for k,v in d.items():
        if v==1 and k>ans:
            ans = k
    return ans