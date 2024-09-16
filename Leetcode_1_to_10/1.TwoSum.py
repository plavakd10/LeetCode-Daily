def two_sum(nums,target):
    dictionary = {}
    for index,value in enumerate(nums):
        complement = target-value
        if complement in dictionary:
            return [dictionary[complement],index]
        dictionary[value]=index




nums = [2,7,11,15]
target = 9
print(two_sum(nums,target))   

nums = [3,2,4]
target = 6
print(two_sum(nums,target))   

nums = [3,3]
target = 6
print(two_sum(nums,target))   