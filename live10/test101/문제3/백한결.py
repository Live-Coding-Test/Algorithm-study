from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]

    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    distance = [-1] * (n + 1)
    distance[1] = 0

    queue = deque([1])

    while queue:
        now = queue.popleft()
        for neighbor in graph[now]:
            if distance[neighbor] == -1:
                distance[neighbor] = distance[now] + 1
                queue.append(neighbor)

    max_distance = max(distance)

    return distance.count(max_distance)