def minSum(nums1, nums2) -> int:
    z1 = nums1.count(0)
    z2 = nums2.count(0)
    s1 = sum(nums1)
    s2 = sum(nums2)
    if (z2==0 and s2<s1+z1) or (z1==0 and s1<s2+z2):
        return -1
    return max(s1+z1,s2+z2)
        