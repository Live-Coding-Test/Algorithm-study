import sys
from collections import defaultdict, deque

def main():
    input = sys.stdin.readline

    N, M, K, X = map(int, input().split())
    graph = defaultdict(list)

    for _ in range(M):
        A, B = map(int, input().split())
        graph[A].append(B)

    distance = [-1] * (N + 1)
    distance[X] = 0

    queue = deque([X])

    while queue:
        current = queue.popleft()

        for neighbor in graph[current]:
            if distance[neighbor] == -1:
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)

    result = [i for i in range(1, N + 1) if distance[i] == K]

    if result:
        for city in sorted(result):
            print(city)
    else:
        print(-1)

if __name__ == "__main__":
    main()