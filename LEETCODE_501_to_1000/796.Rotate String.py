def rotateString(s,goal) -> bool:
    if len(s)!=len(goal):
        return False
    return goal in s+s  