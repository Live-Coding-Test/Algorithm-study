import sys
from collections import *

input = sys.stdin.readline

n = int(input())
m = int(input())
network = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    network[x].append(y)
    network[y].append(x)

visited = [0] * (n + 1)
q = deque([1])
while q:
    x = q.popleft()
    visited[x] = 1
    for nx in network[x]:
        if not visited[nx]:
            visited[nx] = 1
            q.append(nx)

print(sum(visited) - 1)

"""
7
6
1 2
2 3
1 5
5 2
5 6
4 7
"""