import sys
import heapq

input = sys.stdin.readline

n, d = map(int, input().split())

distance = [[] for _ in range(d + 1)]
for i in range(d):
    distance[i].append((i + 1, 1))    # 기본 도로

for _ in range(n):
    start, end, dist = map(int, input().split())
    if end <= d and end - start > dist:
        distance[start].append((end, dist))

dist = [float('inf')] * (d + 1)
heap = [(0, 0)] # (도로 길이, 시작 위치)
while heap:
    cur_dist, cur = heapq.heappop(heap)
    if cur_dist > dist[cur]:
        continue
    for dest, cost in distance[cur]:
        total = cur_dist +  cost
        if total < dist[dest]:
            dist[dest] = total
            heapq.heappush(heap, (total, dest))

print(dist[d])
