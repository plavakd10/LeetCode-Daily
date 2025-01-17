def doesValidArrayExist(derived) -> bool:
    first, last =0,0

    for i in derived:
        if i:
            last=~last
    return first==last   