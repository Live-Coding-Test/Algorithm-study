from collections import * 

def solution(n, edge):
    answer = 0
    
    graph = [[] for _ in range(n + 1)]
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    

    def bfs(x):
        q = deque([x])
        while q:
            x = q.popleft()
            print(graph[x])
            for nei in graph[x]:
                if nei != 0:
                    nei = 0
                    answer += 1
                    q.append(nei)
    bfs(1)

    return answer