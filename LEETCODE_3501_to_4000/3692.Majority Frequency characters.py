from collections import Counter
def majorityFrequencyGroup(s: str) -> str:
    c = Counter(s)
    d = {}
    for k,v in c.items():
        if v in d:
            d[v].append(k)
        else:
            d[v] = [k]    
    return "".join(list(sorted(d.items(), key = lambda x: (-len(x[1]),-x[0])))[0][1])