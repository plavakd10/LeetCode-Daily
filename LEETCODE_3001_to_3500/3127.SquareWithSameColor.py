def canMakeSquare(grid) -> bool:
    def bw(x,y):
        c = [grid[x][y], grid[x][y+1],grid[x+1][y],grid[x+1][y+1]]
        d = {'W':0,'B':0}
        for item in c:
            d[item]+=1
        return d['B']>=3 or d['W']>=3    
    for i in range(2):
        for j in range(2):
            if bw(i,j):
                return True
    return False 