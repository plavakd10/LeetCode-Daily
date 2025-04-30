def findNumbers(nums) -> int:
    return sum([1 for num in nums if len(str(num))%2==0])