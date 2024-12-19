from collections import *


def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]

    answer = []

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' and visited[i][j] == 0:
                q = deque([(i, j)])
                res = int(maps[i][j])
                while q:
                    x, y = q.popleft()
                    visited[x][y] = 1

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if len(maps) > nx >= 0 == visited[nx][ny] and 0 <= ny < len(maps[0]):
                            if maps[nx][ny] != 'X':
                                q.append((nx, ny))
                                visited[nx][ny] = 1
                                res += int(maps[nx][ny])
                answer.append(res)
    if not answer:
        return [-1]
    return sorted(answer)
