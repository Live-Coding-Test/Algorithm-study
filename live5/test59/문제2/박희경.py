import sys

input = sys.stdin.readline

n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

prefix_grid_sum = [[0] * m for _ in range(n)]
prefix_grid_sum[0][0] = grid[0][0]

for i in range(n):
    for j in range(m):
        if i == 0:
            prefix_grid_sum[i][j] = prefix_grid_sum[i][j-1] + grid[i][j]
        elif j == 0:
            prefix_grid_sum[i][j] = prefix_grid_sum[i-1][j] + grid[i][j]
        else:
            prefix_grid_sum[i][j] = grid[i][j] + prefix_grid_sum[i-1][j] + prefix_grid_sum[i][j-1] - prefix_grid_sum[i-1][j-1]

k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())

    i, j, x, y = i - 1, j - 1, x - 1, y - 1

    # 여기부터 다시




"""
2 3
1 2 4
8 16 32
2
1 2 1 2
1 3 2 3
"""