from collections import defaultdict
def countBadPairs(nums) -> int:
    pairs = len(nums)*(len(nums)-1)//2
    good_pairs = 0
    d = defaultdict(int)
    for i in range(len(nums)):
        good_pairs+= d[nums[i]-i]
        d[nums[i]-i]+=1
    return pairs-good_pairs   