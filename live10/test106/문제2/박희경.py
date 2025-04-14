import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]  # 인접리스트 (인접 행렬로 하면 메모리 초과)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))        
    graph[b].append((a, c))

cost = [float('inf')] * (n + 1)
cost[1] = 0
heap = [(0, 1)]    # (최소비용, 시작지점) 

# 가중치가 변동이 있다면 우선순위 큐 사용한 다익스트라
while heap:
    cur_cost, x = heapq.heappop(heap)
    if cur_cost > cost[x]:
        continue
    for nx, w in graph[x]:          
        total = cur_cost + w
        if total < cost[nx]:
            cost[nx] = total
            heapq.heappush(heap, (total, nx))

print(cost[n])
