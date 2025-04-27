def countSubarrays(nums, minK: int, maxK: int) -> int:
    pMin = -1 
    pMax = -1
    bad = -1 
    ans = 0   

    for i,nums in enumerate(nums):
        if nums == minK:
            pMin = i
        if nums == maxK:
            pMax = i
        if nums < minK or nums > maxK:
            bad = i
        if pMin != -1 and pMax != -1:
            ans += max(0, min(pMin, pMax) - bad)

    return ans