from collections import *

def solution(board):
    # 상하좌우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    n = len(board)
    m = len(board[0])
    
    def bfs(x, y, move):
        q = deque([(x, y, move)])
        visited = [[0] * m for _ in range(n)]
        visited[x][y] = 1
        
        while q:
            x, y, move = q.popleft()
            if board[x][y] == 'G':
                return move
            # 'D' 만날 때까지 이동
            for i in range(4):
                nx, ny = x, y
                while 0 <= nx + dx[i] < n and 0 <= ny + dy[i] < m and board[nx + dx[i]][ny + dy[i]] != 'D':
                    nx += dx[i]
                    ny += dy[i]
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny, move + 1))
        return -1
    

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                return bfs(i, j, 0)