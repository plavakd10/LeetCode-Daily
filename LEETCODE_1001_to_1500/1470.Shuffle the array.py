def shuffle(nums,n):
    a = nums[:len(nums)//2]
    b = nums[len(nums)//2:]
    v = []
    for i in range(len(nums)//2):
        v.append(a[i])
        v.append(b[i])
    return v