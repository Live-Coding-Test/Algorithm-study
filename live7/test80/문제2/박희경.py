import sys
from collections import *

input = sys.stdin.readline
n, m = map(int, input().split())
floor = [list(map(str, input().rstrip())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(a, b, current):
    q = deque([(a, b)])
    cnt = 1
    if current == '|':
        direction_range = range(2)
    else:
        direction_range = range(2, 4)
    while q:
        x, y = q.popleft()
        for i in direction_range:
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if floor[nx][ny] == current:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    return cnt


result = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            result += bfs(i, j, floor[i][j])

print(result)

"""
6 9
-||--||--
--||--||-
|--||--||
||--||--|
-||--||--
--||--||-
"""
