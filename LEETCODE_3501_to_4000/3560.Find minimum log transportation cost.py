def minCuttingCost(self, n: int, m: int, k: int) -> int:
    ans = 0
    if n<=k and m<=k:
        return 0
    if n>k and m<=k:
        ans += (n-k)*k
    if m>k and n<=k:
        ans += (m-k)*k
    return ans            
