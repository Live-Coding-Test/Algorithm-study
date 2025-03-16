def solution(board, skill):
    count = 0

    diff = [[0] * (len(board[0])+1) for _ in range(len(board) + 1)]

    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree = -degree

        diff[r1][c1] += degree
        diff[r1][c2+1] -= degree
        diff[r2+1][c1] -= degree
        diff[r2+1][c2+1] += degree

    for i in range(len(board)):
        for j in range(len(board[0])):
            diff[i][j+1] += diff[i][j]

    for i in range(len(board)):
        for j in range(len(board[0])):
            diff[i+1][j] += diff[i][j]

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += diff[i][j]
            if board[i][j] > 0:
                count +=1

    return count