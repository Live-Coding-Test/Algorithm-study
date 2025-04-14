import sys


input = sys.stdin.readline

n = int(input())    # 도시 개수
m = int(input())    # 버스 개수

graph = [[float('inf')] * n for _ in range(n)]
for _ in range(m):
    start, end, cost = map(int, input().split())

    graph[start - 1][end - 1] = min(cost, graph[start - 1][end - 1])
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j: 
                graph[i][j] = 0
                continue
            if graph[i][k] != float('inf') and graph[k][j] != float('inf'):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for row in graph:
    res = []
    for x in row:
        if x == float('inf'):
            res.append(0)
        else:
            res.append(x)
    print(*res)
