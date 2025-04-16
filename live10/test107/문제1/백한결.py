from collections import defaultdict
import heapq
import sys

def main():
    input = sys.stdin.readline
    V, E = map(int, input().strip().split())

    K = int(input())

    graph = defaultdict(list)

    for _ in range(E):
        u, v, w = map(int, input().strip().split())
        graph[u].append((v, w))

    dist = [float('inf')] * (V + 1)
    dist[K] = 0

    pq = []
    heapq.heappush(pq, (0, K))

    while pq:
        cost, now = heapq.heappop(pq)

        if dist[now] < cost:
            continue

        for next, weight in graph[now]:
            newCost = cost + weight
            if newCost < dist[next]:
                dist[next] = newCost
                heapq.heappush(pq, (newCost, next))

    for i in range(1, V + 1):
        if dist[i] == float('inf'):
            print('INF')
        else:
            print(dist[i])


if __name__ == "__main__":
    main()