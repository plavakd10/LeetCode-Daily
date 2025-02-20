def isPalindrome(head) -> bool:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp
    l,r = head, prev
    while r:
        if l.val!=r.val:
            return False
        r = r.next
        l = l.next
    return True  