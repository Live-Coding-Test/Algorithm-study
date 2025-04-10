import sys
from collections import *

input = sys.stdin.readline


# 도시 개수, 도로 개수, 거리 정보, 출발 도시
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [0] * (n + 1)
visited[x] = 1
result = []
q = deque(([(x, 0)]))
while q:
    x, cnt = q.popleft()
    if cnt == k:
        result.append(x)
    for nei in graph[x]:
        if not visited[nei]:
            visited[nei] = 1
            q.append((nei, cnt + 1))

if not result:
    print(-1)
else:
    for res in sorted(result):
        print(res)
