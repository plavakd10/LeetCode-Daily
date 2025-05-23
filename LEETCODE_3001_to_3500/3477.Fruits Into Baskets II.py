def numOfUnplacedFruits(fruits,baskets) -> int:
    n = len(fruits)
    ans = 0
    for f in fruits:
        for i in range(n):
            if f <= baskets[i]:
                baskets[i] = 0
                break
        else:
            ans+=1
    return ans  