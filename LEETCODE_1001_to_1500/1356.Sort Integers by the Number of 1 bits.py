def sortByBits(arr):
    return sorted(arr, key=lambda a: [bin(a).count('1'), a])