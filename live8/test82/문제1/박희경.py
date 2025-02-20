import sys
from collections import *

input = sys.stdin.readline

n, m = map(int,input().split())

picture = []
for _ in range(n):
    picture.append(list(map(int,input().split())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0] * m for _ in range(n)]


def bfs(x, y):
    q = deque([(x, y)])
    size = 1
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if picture[nx][ny] == 1:
                    size += 1
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    return size


cnt = 0
max_extent = 0
for i in range(n):
    for j in range(m):
        if picture[i][j] == 1 and not visited[i][j]:
            max_extent = max(bfs(i, j), max_extent)
            cnt += 1
print(cnt)
print(max_extent)

"""
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1
"""