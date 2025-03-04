def pivotArray(nums, pivot: int):
    smaller = [i for i in nums if i<pivot]
    larger = [i for i in nums if i>pivot]
    return smaller+[pivot]*nums.count(pivot)+larger