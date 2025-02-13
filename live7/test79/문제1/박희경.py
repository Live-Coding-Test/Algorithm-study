import sys

input = sys.stdin.readline
grid = [list(map(str, input().split())) for _ in range(5)]

result = set()


def dfs(a, b, num):
    if len(num) == 6:
        result.add(num)
        return

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx, ny = a + dx[i], b + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, num + grid[nx][ny])


for i in range(5):
    for j in range(5):
        dfs(i, j, grid[i][j])

print(len(result))

"""
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 2 1
1 1 1 1 1
"""
