import sys
from collections import *

input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] * (n + 1) for _ in range(n + 1)]

visited1 = [0] * (n + 1)
visited2 = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for node in graph:
    node.sort()

def dfs(start):
    visited1[start] = 1
    print(start, end=' ')
    if len(graph[start]) != 0:
        for i in graph[start]:
            if not visited1[i]:
                dfs(i)


def bfs(start):
    q = deque([start])
    while q:
        x = q.popleft()
        visited2[x] = 1
        print(x, end=' ')
        for i in graph[x]:
            if not visited2[i]:
                visited2[i] = 1
                q.append(i)

dfs(v)
print()
bfs(v)

"""
4 5 1
1 2
1 3
1 4
2 4
3 4
---
5 5 3
5 4
5 2
1 2
3 4
3 1
"""