import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                visited[nx][ny] = 1
                if grid[nx][ny] == '#':
                    q.append((nx, ny))
    cnt += 1
    return cnt


t = int(input())
for _ in range(t):
    h, w = map(int, input().split())

    grid = []
    for _ in range(h):
        grid.append(list(map(str, input().rstrip())))

    visited = [[0] * w for _ in range(h)]
    result = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '#' and not visited[i][j]:
                result += bfs(i, j)

    print(result)
