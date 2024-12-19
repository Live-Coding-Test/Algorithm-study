import sys

input = sys.stdin.readline

n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]  # [놓친 부분] 0으로 비워두고 자리 수 맞추기

for i in range(1, n + 1):
    for j in range(1, m + 1):
        prefix_sum[i][j] = (
            grid[i - 1][j - 1]
            + prefix_sum[i - 1][j]
            + prefix_sum[i][j - 1]
            - prefix_sum[i - 1][j - 1]
        )

k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())

    result = (
            prefix_sum[x][y]
            - prefix_sum[i - 1][y]
            - prefix_sum[x][j - 1]
            + prefix_sum[i - 1][j - 1]
    )
    print(result)