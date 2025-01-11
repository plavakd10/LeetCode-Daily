def maxProfit(prices: List[int]) -> int:
    l,r = 0,1
    profit = 0
    for r in range(len(prices)):
        if prices[l]<prices[r]:
            profit = max(profit,prices[r]-prices[l])
        else:
            l=r
        r+=1
    return profit 