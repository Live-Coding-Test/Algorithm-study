import sys
from collections import *

input = sys.stdin.readline

n, m, k = map(int, input().split())
grid = [['.' for _ in range(m)] for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    grid[r - 1][c - 1] = '#'

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0 for _ in range(m)] for _ in range(n)]


def bfs(a, b):
    size = 1
    q = deque([(a, b)])
    visited[a][b] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if grid[nx][ny] == '#':
                    size += 1
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    return size


result = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == '#':
            result = max(result, bfs(i, j))

print(result)

"""
3 4 5
3 2
2 2
3 1
2 3
1 1
"""
