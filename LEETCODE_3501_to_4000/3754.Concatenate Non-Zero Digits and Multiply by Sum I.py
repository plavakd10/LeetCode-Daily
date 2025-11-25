def sumAndMultiply(n) -> int:
    x = 0
    s = 0
    for ele in str(n):
        if ele!="0":
            m = int(ele)
            x = x*10 + m
            s += m
    return x*s 