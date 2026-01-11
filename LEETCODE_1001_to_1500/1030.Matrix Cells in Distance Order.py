def allCellsDistOrder(rows: int, cols: int, rCenter: int, cCenter: int):
    def distance(point):
        xi,yi = point
        return abs(xi-rCenter) + abs(yi-cCenter)

    p = [(i,j) for i in range(rows) for j in range(cols)]
    return sorted(p,key=distance) 