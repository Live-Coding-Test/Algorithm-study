from collections import *

def solution(board):
    answer = 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    n = len(board)
    m = len(board[0])
    
    def bfs(x, y):
        q = deque([(x, y)])
        cnt = 0
        while q:
            x, y = q.popleft()
            cnt += 1
            for i in range(4):
                nx = x + dx[i] 
                ny = y + dy[i]
                if 0 <= nx < n or 0 <= y < m or board[x][y] == 'D':
                    if board[nx][ny] == 'G':
                        return cnt
                    q.append((nx, ny))
            
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                cnt += bfs(i, j)
    print(cnt)
    
    return answer