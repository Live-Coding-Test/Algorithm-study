def solution(n, computers):
    visited = [False] * n

    def dfs(v):
        visited[v] = True
        for i in range(n):
            if computers[v][i] == 1 and not visited[i]:
                dfs(i)

    count = 0

    for i in range(n):
        if not visited[i]:
            dfs(i)
            count += 1

    return count