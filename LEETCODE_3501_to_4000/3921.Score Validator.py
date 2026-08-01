def scoreValidator(self, events: list[str]) -> list[int]:
    score = 0
    counter = 0
    for i in range(len(events)):
        if events[i] == "W":
            counter+=1
        if counter == 10:
            break   
        if events[i] in ["0","1","2","3","4","6"]:
            score+=int(events[i])
        if events[i] in ["WD","NB"]:
            score+=1
    return [score,counter] 