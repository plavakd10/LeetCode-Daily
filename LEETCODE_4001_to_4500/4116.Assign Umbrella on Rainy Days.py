def assignUmbrella(self, rain: list[int]) -> list[str]:
    n = len(rain)
    d = 0
    r = [""] * n
    for i in range(n):
        if rain[i] == 0:
            r[i] = "None"
            continue
        if i == n-1 or rain[i+1] == 0:
            r[i] = "Bob"
            d+=1
            continue
        if d>=0:
            r[i] = "Alice"
            d-=1
            continue
        r[i]="Bob"
        d+=1
    return r