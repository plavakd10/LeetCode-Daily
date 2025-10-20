def finalValueAfterOperations(operations) -> int:
    s = 0
    for op in operations:
        if op == "X++" or op == "++X":
            s+=1
        else:
            s-=1
    return s            
        