def solution(n, computers):
    answer = 0
    
    visited = [False] * n
    
    def dfs(x):
        visited[x] = True
        for i in range(n):
            if not visited[i] and computers[x][i] == 1:
                dfs(i)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    return answer