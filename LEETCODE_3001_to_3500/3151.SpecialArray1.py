def isArraySpecial(nums) -> bool:
    for i in range(len(nums)-1):
        if nums[i]%2==nums[i+1]%2:
            return False
    return True

ip1 = [1]
ip2 = [2,1,4]
ip3 = [4,3,1,6]

print(isArraySpecial(ip1))
print(isArraySpecial(ip2))
print(isArraySpecial(ip3))  