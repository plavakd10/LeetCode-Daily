def queryResults(limit,queries):
    balls = {}
    colors = {}
    s = set()
    res = []
    for ball,color in queries:
        if ball in balls:
            prev_c = balls[ball]
            colors[prev_c]-=1
            if colors[prev_c]==0:
                s.remove(prev_c)
        balls[ball]=color
        colors[color]=colors.get(color,0)+1
        s.add(color)
        res.append(len(s))
    return res     