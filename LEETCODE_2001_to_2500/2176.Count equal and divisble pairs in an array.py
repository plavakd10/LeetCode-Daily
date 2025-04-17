from collections import defaultdict,List
def countPairs(nums: List[int], k: int) -> int:
    d = defaultdict(list)
    count = 0
    for i,v in enumerate(nums):
        if v in d:
            for x in d[v]:
                if (i*x)%k==0:
                    count+=1
        d[v].append(i)      
    return count