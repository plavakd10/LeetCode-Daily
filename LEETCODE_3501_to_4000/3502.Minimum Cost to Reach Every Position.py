def minCosts(cost):
    arr = [cost[0]]
    for i in range(1,len(cost)):
        arr.append(min(arr[i-1],cost[i]))
    return arr   