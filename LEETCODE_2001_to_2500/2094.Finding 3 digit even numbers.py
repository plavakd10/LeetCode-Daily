from collections import Counter
def findEvenNumbers(digits):
    d = Counter(digits)
    ans = []
    for n in range(100,1000,2):
        if not Counter([int(i) for i in str(n)])-d:
            ans.append(n)
    return ans 