import math
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
r = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    r[a].append(b)
    r[b].append(a)


def dfs(x, target, depth):
    if x == target:
        return depth
    if len(r[x]) != 0:
        for i in r[x]:
            if not visited[x]:
                visited[x] = 1
                depth += 1
                dfs(i, target, depth)


min_kb = float("-inf")
for i in range(1, n + 1):
    i_kb = 0
    for j in range(1, n + 1):
        if i != j:
            visited = [0] * (n + 1)
            i_kb += dfs(i, j)
    min_kb = min(min_kb, i_kb)


"""
5 5
1 3
1 4
4 5
4 3
3 2
"""
