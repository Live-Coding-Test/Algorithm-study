import sys
from collections import *

input = sys.stdin.readline

n, m = map(int, input().split())
r = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    r[a].append(b)
    r[b].append(a)


def bfs(x, target, depth):
    visited = [0] * (n + 1)
    q = deque([(x, depth)])
    visited[x] = 1
    while q:
        x, depth = q.popleft()
        if x == target:
            return depth
        for nx in r[x]:
            if not visited[nx]:
                visited[nx] = 1
                q.append((nx, depth + 1))


kb = [float("inf")] + []
for i in range(1, n + 1):
    i_kb = 0
    for j in range(1, n + 1):
        if i != j:
            i_kb += bfs(i, j, 0)
    kb.append(i_kb)
print(kb.index(min(kb)))

"""
5 5
1 3
1 4
4 5
4 3
3 2
"""
