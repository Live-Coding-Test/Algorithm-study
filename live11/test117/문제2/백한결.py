import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)


def main():
    input = sys.stdin.readline

    N = int(input())
    graph = defaultdict(list)

    for _ in range(N-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    dp = [[0, 0] for _ in range(N+1)]
    visited = [False] * (N+1)

    def dfs(node):
        visited[node] = True
        dp[node][0] = 0
        dp[node][1] = 1

        for child in graph[node]:
            if not visited[child]:
                dfs(child)
                dp[node][0] += dp[child][1]
                dp[node][1] += min(dp[child][0], dp[child][1])

    dfs(1)
    print(min(dp[1][0], dp[1][1]))

if __name__ == '__main__':
    main()