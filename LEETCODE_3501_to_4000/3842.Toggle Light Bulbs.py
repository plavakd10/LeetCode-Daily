def toggleLightBulbs(bulbs):
    s = set()
    for b in bulbs:
        if b in s: 
            s.remove(b)
        else:
            s.add(b)
    return sorted(list(s))