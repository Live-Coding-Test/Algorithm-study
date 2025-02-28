import sys
from collections import *

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == '#':
                grid[nx][ny] = '.'
                q.append((nx, ny))
    return True


t = int(input())
for _ in range(t):
    h, w = map(int, input().split())
    grid = []
    for _ in range(h):
        grid.append(list(map(str, input().rstrip())))

    cnt = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '#':
                if bfs(i, j):
                    cnt += 1
    print(cnt)


"""
2
4 4
#.#.
.#.#
#.##
.#.#
3 5
###.#
..#..
#.###
"""
