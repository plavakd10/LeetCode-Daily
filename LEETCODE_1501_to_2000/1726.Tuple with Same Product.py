from collections import defaultdict
def tupleSameProduct(nums) -> int:
    count1 = defaultdict(int)
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            p = nums[i]*nums[j]
            count1[p]+=1
    ans = 0 
    for v in count1.values():
        pairs = v*(v-1)//2
        ans+=8*pairs
    return ans 