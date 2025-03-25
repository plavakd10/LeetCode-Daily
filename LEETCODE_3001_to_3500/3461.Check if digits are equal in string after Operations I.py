def hasSameDigits(s: str) -> bool:
    st = s
    while len(st)>2:
        st1 = ""
        for i in range(len(st)-1):
            st1+=str((int(st[i])+int(st[i+1]))%10)
        st = st1    
    return st[0]==st[1]