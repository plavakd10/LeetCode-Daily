def eventualSafeNodes(graph):
    n = len(graph)
    safe = {}
    def dfs(i):
        if i in safe:
            return safe[i]
        safe[i]=False
        for nei in graph[i]:
            if not dfs(nei):
                return safe[i]
        safe[i]= True
        return safe[i]

    ans = []
    for i in range(n):
        if dfs(i):
            ans.append(i)
    return ans                        