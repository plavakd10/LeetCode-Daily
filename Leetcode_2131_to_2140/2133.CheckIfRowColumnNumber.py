def checkValid(matrix) -> bool:
    l = [0]*len(matrix)
    for i in matrix:
        if len(set(i))!=len(matrix):
            return False
        for j in range(len(i)):
            l[j]+=i[j]
    return len(set(l))==1  