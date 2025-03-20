def dfs(node, graph, visited):
    visited[node] = True
    size = 1
    
    for neighbor in graph[node]:
        if not visited[neighbor]:
            size += dfs(neighbor, graph, visited)
    
    return size

def solution(n, wires):
    answer = float('inf')
    
    for i in range(len(wires)):
        count = 0
        w_copy = wires[:]
        w_copy.pop(i)
        print(w_copy)
        graph = [[] for _ in range(n+1)]
    
        for wire in w_copy:
            graph[wire[0]].append(wire[1])
            graph[wire[1]].append(wire[0])
    
        visited = [False] * (n + 1)
        size_one = dfs(w_copy[0][0], graph, visited)
        size_two = n - size_one
        
        answer = min(answer, abs(size_one - size_two))
        
    print(count)
    return answer