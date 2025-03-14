def solution(board, skill):
    answer = len(board)*len(board[0])
    
    # broken = set()
    
    for s in skill:
        stype, r1, c1, r2, c2, degree = s
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                check = False
                if stype == 1:
                    if board[r][c] <= 0:
                        check = True
                    board[r][c] -= degree
                    if board[r][c] <= 0:
                        if not check:
                            answer -= 1
                elif stype == 2:
                    if board[r][c] <= 0:
                        check = True
                    board[r][c] += degree
                    if board[r][c] > 0:
                        if check:
                            answer += 1
    # for i in range(len(board)):
    #     for j in range(len(board[0])):
    #         if board[i][j] > 0:
    #             answer += 1
    # print(len(board)*len(board[0])-len(broken))
    return answer