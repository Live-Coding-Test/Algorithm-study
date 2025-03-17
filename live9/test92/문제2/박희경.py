def solution(board, skill):
    answer = 0
    n = len(board) 
    m = len(board[0])   
    
    degree = [[0] * (m + 1) for _ in range(n + 1)]
    for type, r1, c1, r2, c2, d in skill:
        d = -d if type == 1 else d
        degree[r1][c1] += d
        degree[r1][c2 + 1] -= d
        degree[r2 + 1][c1] -= d
        degree[r2 + 1][c2 + 1] += d
    
    # 행기준 -> 
    for i in range(n):
        for j in range(m):
            degree[i][j+1] += degree[i][j]
    
    # 열 기준 ↓
    for j in range(m):
        for i in range(n):
            degree[i+1][j] += degree[i][j]
    
    for i in range(n):
        for j in range(m):
            board[i][j] += degree[i][j]
    

    return sum(1 for row in board for cell in row if cell > 0)