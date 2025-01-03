from collections import deque

n = int(input())

ary = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

def bfs(x, y):
    q = deque([])
    q.append([x, y, ary[x][y]])

    while q:
        v = q.popleft()
        visited[v[0]][v[1]] = 1
        if v[2] == -1:
            print("HaruHaru")
            return

        nx = v[0] + v[2]
        if nx < n and visited[nx][v[1]] == 0:
            q.append([nx, v[1], ary[nx][v[1]]])
        ny = v[1] + v[2]
        if ny < n and visited[v[0]][ny] == 0:
            q.append([v[0], ny, ary[v[0]][ny]])

    print("Hing")

bfs(0, 0)
