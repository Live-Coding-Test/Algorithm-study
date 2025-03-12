from collections import *


def solution(n, computers):
    answer = 0
    visited = [0] * (n + 1)

    def dfs(x):
        visited[x] = 1
        for i in range(n):
            if not visited[i] and computers[x][i] == 1:
                dfs(i)

    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1

    return answer