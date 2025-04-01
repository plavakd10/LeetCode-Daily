def mostPoints(questions) -> int:
    n = len(questions)
    cache = [0]*n

    for i in reversed(range(n)):
        score, brainpower = questions[i]
        next_index = i+1 + brainpower
        choose = score + (cache[next_index] if next_index < n else 0)
        skip = cache[i+1] if i+1 <n else 0 
        cache[i] = max(skip,choose)
    return cache[0]    