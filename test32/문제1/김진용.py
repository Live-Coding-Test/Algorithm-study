import sys
sys.setrecursionlimit(10**6)
test = int(input())
for t in range(test):
    h, w = map(int, input().split())
    graph = []
    visited = [[False] * w for _ in range(h)]
    for _h in range(h):
        graph.append(list(map(str, input())))


    def dfs(x, y):
        visited[x][y] = True

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] != '.':
                if not visited[nx][ny]:
                    dfs(nx, ny)


    cnt = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and graph[i][j] == '#':
                dfs(i, j)
                cnt += 1
    print(cnt)