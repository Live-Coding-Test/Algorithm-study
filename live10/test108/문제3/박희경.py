"""
w / 리프노드 수 
리프노드 개수 찾는 문제 ? !
"""

import sys
sys.setrecursionlimit(10**6)    # 파이썬 기본 재귀 깊이 1000 문제에선 n이 10^5이기 때문에 RecursionError 발생
input = sys.stdin.readline

n, w = map(int, input().split())
tree = [[] for _ in range(n + 1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)
    
visited = [0] * (n + 1)
cnt = 0
def dfs(x):
    global cnt
    visited[x] = 1
    is_leaf = True
    for nei in tree[x]:
        if not visited[nei]:
            is_leaf = False
            dfs(nei)
    if is_leaf:
        cnt += 1

dfs(1)
print(w / cnt)
