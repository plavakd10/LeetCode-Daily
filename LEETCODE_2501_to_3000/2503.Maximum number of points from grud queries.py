from heapq import heappop, heappush
def maxPoints(grid, queries):
    rows, cols = len(grid), len(grid[0])

    q = [(n,i) for i,n in enumerate(queries)]
    q.sort()

    min_heap = [(grid[0][0],0,0)]
    visit = set([(0,0)])
    res = [0]*len(queries)
    pts = 0

    for limit, index in q:
        while min_heap and min_heap[0][0]<limit:
            val, r , c = heappop(min_heap)
            pts+=1
            neighbors = [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]
            for nr, nc in neighbors:
                if (0<=nr<rows and 0<=nc<cols and (nr,nc) not in visit):
                    heappush(min_heap, (grid[nr][nc], nr, nc))
                    visit.add((nr,nc))
        res[index] = pts
    return res