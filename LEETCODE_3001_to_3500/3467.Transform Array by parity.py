def transformArray(nums):
    odd_count = 0
    even_count = 0
    for i in nums:
        if i%2==0:
            even_count+=1
        else:
            odd_count+=1
    return ([0]*even_count)+([1]*odd_count)