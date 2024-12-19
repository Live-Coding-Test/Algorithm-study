from collections import deque
def bfs(maps, x, y, visited):
    total = 0
    queue = deque([(x, y)])

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    visited[x][y] = 1

    while queue:
        cx, cy = queue.popleft()
        # print(maps[cx][cy])
        visited[cx][cy] = 1

        total += int(maps[cx][cy])

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and visited[nx][ny] == 0 and maps[nx][ny] != 'X':
                queue.append((nx, ny))
                visited[nx][ny] = 1
    return total

def solution(maps):
    visited = []
    for i in range(len(maps)):
        visited.append(list([0] * len(maps[0])))

    eat = []
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' and visited[i][j] == 0:
                eat.append(bfs(maps, i, j, visited))

    if eat:
        return sorted(eat)
    else:
        return [-1]


print(solution(["X591X", "X1X5X", "X231X", "1XXX1"]))
print(solution(["XXX", "XXX", "XXX"]))
