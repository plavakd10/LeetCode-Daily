def clearDigits(s) -> str: 
    st = []
    for char in s:
        if char.isdigit():
            while st and st[-1].isdigit():
                st.pop()
            if st:
                st.pop()
        else:
            st.append(char)
    return ''.join(st)                    
        