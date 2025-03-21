def solution(board, skill):
    answer = 0
    
    n = len(board)
    m = len(board[0])
    
    degree = [[0] * (m + 1) for _ in range(n + 1)]
    for type, r1, c1, r2, c2, d in skill:
        if type == 1: d = -d
        degree[r1][c1] += d
        degree[r1][c2 + 1] -= d
        degree[r2 + 1][c1] -= d
        degree[r2 + 1][c2 + 1] += d
    
    for i in range(n - 1):
        for j in range(m):
            degree[i+1][j] += degree[i][j]
        
    for j in range(m):
        for i in range(n):
            degree[i][j+1] += degree[i][j]
    

    for i in range(n):
        for j in range(m):
            board[i][j] += degree[i][j]
            if board[i][j] > 0:
                answer += 1
    return answer