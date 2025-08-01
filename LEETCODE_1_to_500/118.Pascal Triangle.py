def generate(numRows: int):
    ans = [[1]]
    for i in range(1, numRows):
        t = []
        tmp = [0] + ans[-1] + [0]
        for k in range(len(tmp)-1):
            t.append(tmp[k]+tmp[k+1])
        ans.append(t)
    return ans  