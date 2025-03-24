def solution(board, skill):
    count = 0

    prefix = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]

    for type, r1, c1, r2, c2, degree in skill:

        if type == 1:
            degree = -degree

        prefix[r1][c1] += degree
        prefix[r1][c2 + 1] -= degree
        prefix[r2 + 1][c1] -= degree
        prefix[r2 + 1][c2 + 1] += degree

    # 세로 누적합
    for i in range(len(board)):
        for j in range(len(board[0])):
            prefix[i][j + 1] += prefix[i][j]

    # 가로 누적합
    for i in range(len(board)):
        for j in range(len(board[0])):
            prefix[i + 1][j] += prefix[i][j]

    # prefix를 board에 반영
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += prefix[i][j]

            if board[i][j] > 0:
                count += 1

    return count