"""
dp[현재노드] = min(dp[자식노드][얼리어답터인 경우;1], dp[자식노드][아닌 경우;0])
"""

import sys
from collections import *
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

graph = defaultdict(list)
n = int(input())
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [[0, 0] for _ in range(n + 1)]     # [노드번호][얼리어답터 체크]
visited = [0 for _ in range(n + 1)]
def dfs(start):
    visited[start] = 1
    if len(graph[start]) == 0:
        dp[start][1] = 1
        dp[start][0] = 0
    else:
        for i in graph[start]:
            if not visited[i]:
                dfs(i)
                dp[start][1] += min(dp[i][0], dp[i][1])
                dp[start][0] += dp[i][1]
        dp[start][1] += 1

dfs(1)
print(min(dp[1][0], dp[1][1]))