def reverseByType(s: str) -> str:
    dup = ""
    alpha = []
    spec = []
    for ch in s:
        if ch.isalpha():
            alpha.append(ch)
        else:
            spec.append(ch)
    for ch in s:
        if ch.isalpha():
            dup+=alpha.pop()
        else:
            dup+=spec.pop()
    return dup