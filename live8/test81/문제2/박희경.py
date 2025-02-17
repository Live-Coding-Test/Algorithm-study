import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
network = [[] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    network[x].append(y)
    network[y].append(x)

# [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]