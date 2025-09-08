def getNoZeroIntegers(self, n: int):
    for i in range(1,n):
        if self.check0(i) and self.check0(n-i):
            return [i,n-i]
def check0(self,n):
    return "0" not in str(n)