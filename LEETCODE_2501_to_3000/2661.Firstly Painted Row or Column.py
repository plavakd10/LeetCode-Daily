def firstCompleteIndex(arr,mat) -> int:
    rows,cols = len(mat),len(mat[0])
    mapping = {}
    for r in range(rows):
        for c in range(cols):
            mapping[mat[r][c]] = (r,c)
    row_count = [0]*rows
    col_count = [0]*cols

    for i in range(len(arr)):
        r,c = mapping[arr[i]]
        row_count[r]+=1
        col_count[c]+=1
        if col_count[c]==rows or row_count[r] == cols:
            return i  