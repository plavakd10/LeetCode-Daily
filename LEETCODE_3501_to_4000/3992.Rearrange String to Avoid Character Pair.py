def rearrangeString(self, s: str, x: str, y: str) -> str:
    if (x not in s) or (y not in s):
        return s
    s1 = list()
    for ch in s:
        if ch not in [x,y]:
            s1.append(ch)
    return s.count(y)*y + s.count(x)*x + "".join(s1)  