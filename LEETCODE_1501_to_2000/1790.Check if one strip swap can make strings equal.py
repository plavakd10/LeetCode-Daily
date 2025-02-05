def areAlmostEqual(s1: str, s2: str) -> bool:
    indices = []
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            indices.append(i)
        if len(indices)>2:
            return False
    if len(indices)==2:
        i,j = indices
        if s1[i]==s2[j] and s1[j]==s2[i]:
            return True
        return False                
    return len(indices)==0 