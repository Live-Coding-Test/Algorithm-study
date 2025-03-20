from collections import *
        
        

def solution(n, wires):
    
    def create_graph(wires):
        graph = [[] for _ in range(n + 1)]

        for v1, v2 in wires:
            graph[v1].append(v2)
            graph[v2].append(v1)
        return graph
        
    def bfs(graph, x, visited):
        cnt = 1
        q = deque([x])
        visited[x] = 1
        while q: 
            x = q.popleft()
            for nx in graph[x]:
                if not visited[nx]:
                    visited[nx] = 1
                    cnt += 1
                    q.append(nx)
        return cnt
    
    answer = float('inf')
    
    # 모든 간선 하나씩 끊어보기
    for i in range(len(wires)):
        tmp = wires[:]
        del tmp[i]
        tmp_graph = create_graph(tmp)
        
        visited = [0] * (n + 1)
        count = []
        
        for num in range(1, n + 1):
            if not visited[num]:
                count.append(bfs(tmp_graph, num, visited))
        
        diff = abs(count[0] - count[1])
        answer = min(answer, diff)

    return answer