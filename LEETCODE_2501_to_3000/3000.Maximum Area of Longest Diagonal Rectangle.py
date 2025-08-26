def areaOfMaxDiagonal(dimensions) -> int:
    max_area = 0
    max_diag = 0
    for dim in dimensions:
        l = dim[0]
        b = dim[1]
        diag = l*l+b*b
        if diag > max_diag or (diag == max_diag and l*b > max_area):
            max_diag = diag
            max_area = l*b
    return max_area        


        