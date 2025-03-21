from collections import deque


def solution(board):
    map = [list(row) for row in board]

    G = (0, 0)
    R = (0, 0)

    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 'R':
                R = (i, j)
            elif map[i][j] == 'G':
                G = (i, j)

    return bfs(map, G, R)


def bfs(map, G, R):
    queue = deque([(R[0], R[1], 0)])

    visited = [[False] * len(map[0]) for _ in range(len(map))]
    visited[R[0]][R[1]] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y, move = queue.popleft()

        if (x, y) == G:
            return move

        for dx, dy in directions:
            nx, ny = x, y
            while 0 <= nx + dx < len(map) and 0 <= ny + dy < len(map[0]) and map[nx + dx][ny + dy] != 'D':
                nx += dx
                ny += dy

            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, move + 1))

    return -1