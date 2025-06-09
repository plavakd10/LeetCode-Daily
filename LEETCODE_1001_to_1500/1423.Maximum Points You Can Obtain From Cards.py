def maxScore(cardPoints, k: int) -> int:
    sum_left, sum_right = sum(cardPoints[:k]), 0
    res = sum_left
    for i in range(k):
        sum_left -= cardPoints[k-i-1]
        sum_right += cardPoints[len(cardPoints)-1-i]
        res = max(res,sum_left+sum_right)
    return res    