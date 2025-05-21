import sys
import heapq
from collections import *

input = sys.stdin.readline

n, m = map(int, input().split())
graph = defaultdict(list)
idx = [0] * (n + 1)    # 진입 차수

for _ in range(m):
    a, b = map(int, input().split())    # a번은 b번 보다 먼저 
    graph[a].append(b)
    idx[b] += 1

heap = []
for i in range(1, n + 1):
    if idx[i] == 0:
        heapq.heappush(heap, i)

res = []
while heap:
    now = heapq.heappop(heap)
    res.append(now)
    for nxt in graph[now]:
        idx[nxt] -= 1
        if idx[nxt] == 0:
            heapq.heappush(heap, nxt)

print(*res)

