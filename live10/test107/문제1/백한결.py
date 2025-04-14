from collections import defaultdict
import heapq

def main():
    V, E = map(int, input().strip().split())

    K = int(input())

    graph = defaultdict(list)

    for _ in range(E):
        u, v, w = map(int, input().strip().split())
        graph[u].append((v, w))

    dist = [float('inf') for _ in range(V)]
    dist[K-1] = 0

    pq = []
    heapq.heappush(pq, (0, K))

    while pq:
        cost, now = heapq.heappop(pq)

        if dist[now-1] < cost:
            continue

        for next, weight in graph[now]:
            newCost = cost + weight
            if newCost < dist[next-1]:
                dist[next-1] = newCost
                heapq.heappush(pq, (newCost, next))

    for d in dist:
        if d == float('inf'):
            print('INF')
        else:
            print(d)

if __name__ == "__main__":
    main()