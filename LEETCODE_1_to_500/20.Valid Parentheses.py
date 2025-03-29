def isValid(s: str) -> bool:
    st = []
    mapping = {
            ")":"(",
            "}":"{",
            "]":"["
    }

    for ch in s:
        if ch in mapping.values():
            st.append(ch)
        elif ch in mapping.keys():
            if not st or mapping[ch]!=st.pop():
                return False
    return not st 