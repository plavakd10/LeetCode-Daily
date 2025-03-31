def putMarbles(weights, k: int) -> int:
    l = len(weights)-1
    weight_arr = [weights[i]+weights[i+1] for i in range(l)]
    weight_arr.sort()
    ans = 0
    for i in range(k-1):
        ans+= weight_arr[-1-i]-weight_arr[i]
    return ans 