def checkZeroOnes(s) -> bool:
    current_1 = current_0 = best_1 = best_0 = 0
    for i in s:
        if i == "1":
            current_0 = 0
            current_1 +=1
        else:
            current_1 = 0
            current_0 +=1
        best_0 = max(best_0,current_0)
        best_1 = max(best_1,current_1)
    return best_1 > best_0            
                   