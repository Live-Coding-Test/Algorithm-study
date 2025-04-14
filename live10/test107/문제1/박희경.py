import sys
import heapq

input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())

graph = [[] for _ in range(v + 1)]
for _ in range(e):
    start, end, weight = map(int, input().split())
    graph[start].append((end, weight))

dist = [float('inf')] * (v + 1)
dist[k] = 0
heap = [(0, k)]  # (거리, 노드)

while heap:
    cur_dist, node = heapq.heappop(heap)
    if cur_dist > dist[node]:
        continue
    for next_node, weight in graph[node]:
        total = cur_dist + weight
        if total < dist[next_node]:
            dist[next_node] = total
            heapq.heappush(heap, (total, next_node))


for i in range(1, v + 1):
    if dist[i] == float('inf'):
        print('INF')
    else:
        print(dist[i])     

"""
5 6
1
5 1 1 
1 2 2 
1 3 3
2 3 4
2 4 5
3 4 6
"""