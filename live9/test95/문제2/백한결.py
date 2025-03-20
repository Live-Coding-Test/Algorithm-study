def solution(n, wires):

    min_difference = float('inf')

    for i in range(len(wires)):
        graph = {j: [] for j in range(1, n+1)}

        for j, (v1, v2) in enumerate(wires):
            if i != j:
                graph[v1].append(v2)
                graph[v2].append(v1)

        visited = [False] * (n+1)
        count = dfs(1, graph, visited)

        min_difference = min(min_difference, abs(count-(n-count)))

    return min_difference


def dfs(start, graph, visited):
    visited[start] = True
    count = 1

    for neighbor in graph[start]:
        if not visited[neighbor]:
            count += dfs(neighbor, graph, visited)

    return count

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))