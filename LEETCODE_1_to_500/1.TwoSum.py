def two_sum(nums,target):
    dictionary = {}
    for index,value in enumerate(nums):
        complement = target-value
        if complement in dictionary:
            return [dictionary[complement],index]
        dictionary[value]=index
