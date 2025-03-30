def partitionLabels(self, s: str):
    lastIndex = {}

    for i,v in enumerate(s):
        lastIndex[v]=i

    res = []
    size,end = 0,0
    for i,v in enumerate(s):
        size+=1
        end = max(end,lastIndex[v])
        if i==end:
            res.append(size)
            size = 0
    return res   