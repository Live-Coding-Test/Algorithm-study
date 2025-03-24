def solution(board, skill):
    n = len(board)
    m = len(board[0])
    
    acc = [[0] * (m + 1) for _ in range(n + 1)]
    
    # skill 명령 누적합 배열에 저장
    for t, r1, c1, r2, c2, degree in skill:
        diff = degree if t == 2 else -degree
        acc[r1][c1] += diff
        acc[r1][c2 + 1] -= diff
        acc[r2 + 1][c1] -= diff
        acc[r2 + 1][c2 + 1] += diff
    
    # 가로 누적합
    for i in range(n):
        for j in range(1, m):
            acc[i][j] += acc[i][j - 1]
    
    # 세로 누적합
    for j in range(m):
        for i in range(1, n):
            acc[i][j] += acc[i - 1][j]
    
    answer = 0
    for i in range(n):
        for j in range(m):
            board[i][j] += acc[i][j]
            if board[i][j] > 0:
                answer += 1
    
    return answer
