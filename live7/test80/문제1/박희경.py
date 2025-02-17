import sys
from collections import *

input = sys.stdin.readline

n, k = map(int, input().split())
visited = [0] * (10 ** 5 + 1)


def bfs(x):
    q = deque([x])
    while q:
        x = q.popleft()
        if x == k:
            return visited[x]
        for nx in (x * 2, x - 1, x + 1):
            if 0 <= nx <= 10 ** 5 and not visited[nx]:
                if nx == 2 * x:
                    visited[nx] = visited[x]
                else:
                    visited[nx] = visited[x] + 1
                q.append(nx)


print(bfs(n))
