def elevatorRequests(self, n: int, requests: list[int]) -> int:
    total = 0
    for i in range(len(requests)-1):
        total += abs(requests[i]-requests[i+1])
    return total + requests[0]