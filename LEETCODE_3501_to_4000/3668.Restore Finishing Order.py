def recoverOrder(order, friends):
    ans = []
    for pos in order:
        if pos in friends:
            ans.append(pos)
    return ans 