import sys

input = sys.stdin.readline

n = int(input())
color = [list(map(int, input().split())) for _ in range(n)]

for i in range(n-1):
    min_cost = min(color[i])
    min_idx = color[i].index(min_cost)
    for j in range(3):
        if j != min_idx:
            color[i+1][j] += min_cost
        else:
            color[i][min_idx] = float('inf')
            color[i+1][j] += min(color[i])

print(min(color[-1]))
