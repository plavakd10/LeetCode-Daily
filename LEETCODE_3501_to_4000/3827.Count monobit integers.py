def countMonobit(n: int) -> int:
    count = 1
    k = 1
    while ((1<<k)-1) <=n:
        count+=1
        k+=1
    return count 