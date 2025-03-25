def checkValidCuts(n,rectangles) -> bool:
    x = [(r[0],r[2]) for r in rectangles]
    y = [(r[1],r[3]) for r in rectangles]
    x.sort()
    y.sort()

    def count(intervals):
        c = 0
        prev_end = -1
        for start, end in intervals:
            if prev_end <= start:
                c+=1
            prev_end = max(prev_end, end)
        return c        

    return max(count(x),count(y))>=3