from math import sqrt
def repairCars(ranks, cars: int) -> int:
    def count_rep(time):
        c = 0
        for r in ranks:
            c+= int(sqrt(time/r))
        return c    
    l,r = 1,ranks[0]*cars*cars
    res = -1
    while l<=r:
        m = (l+r)//2
        repaired = count_rep(m)
        if repaired>=cars:
            res=m
            r=m-1
        else:
            l=m+1
    return res
        