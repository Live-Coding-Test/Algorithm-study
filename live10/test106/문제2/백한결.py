import heapq
from collections import defaultdict

def main():
    n, m = map(int, input().split())

    cityMap = defaultdict(list)

    for _ in range(m):
        a, b, c = map(int, input().split())
        cityMap[a].append((b, c))
        cityMap[b].append((a, c))

    dist = [float('inf')] * (n + 1)
    dist[1] = 0

    pq = []
    heapq.heappush(pq, (0, 1))

    while pq:
        cost, now = heapq.heappop(pq)

        if dist[now] < cost:
            continue

        for next_node, weight in cityMap[now]:
            new_cost = cost + weight
            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))

    print(dist[n])

if __name__ == "__main__":
    main()