def getDecimalValue(head) -> int:
    s = ""
    while head:
        s+= str(head.val)
        head = head.next
    b = int(s)
    d, p = 0, 0
    while b:
        d += (b % 10) * (2 ** p)
        b //= 10
        p += 1
    return d 