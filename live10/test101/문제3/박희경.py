from collections import * 

def solution(n, edge):
    
    graph = [[] for _ in range(n + 1)]
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [0] * (n + 1)
    visited[1] = 1

    def bfs(x):
        q = deque([x])
        while q:
            x = q.popleft()
            for nei in graph[x]:
                if not visited[nei]: 
                    visited[nei] = visited[x] + 1
                    q.append(nei)
    bfs(1)

    return visited.count(max(visited))