def countServers(grid) -> int:
    rows = len(grid)
    cols = len(grid[0])
    row = [0]*rows
    col = [0]*cols

    for r in range(rows):
        for c in range(cols):
            if grid[r][c]==1:
                row[r]+=1
                col[c]+=1

    ans = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] and max(row[r],col[c])>1:
                ans+=1
    return ans    