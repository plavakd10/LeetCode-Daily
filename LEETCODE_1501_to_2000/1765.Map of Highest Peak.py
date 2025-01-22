from collections import deque


def highestPeak(isWater):
    rows = len(isWater)
    cols = len(isWater[0])
    q = deque()
    visited = set()
    res = [[-1]*cols for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if isWater[r][c]:
                q.append((r,c))
                visited.add((r,c))
                res[r][c]=0
    while q:
        r,c = q.popleft()
        h = res[r][c]

        neighbors = [[r+1,c],[r,c+1],[r-1,c],[r,c-1]]

        for nr,nc in neighbors:
            if (nr<0 or nc<0 or 
            nr==rows or nc==cols or 
            (nr,nc) in visited):
                continue
            q.append((nr,nc))
            visited.add((nr,nc))
            res[nr][nc] = h+1
    return res                        
