def solution(n):
    answer = [[0] * i for i in range(1, n + 1)]    # 삼각형 배열
    
    
    x, y = -1, 0    # 첫 시작 (아래방향부터 시작하기 위해)
    num = 1
    
    for i in range(n):  # 방향 전환은 n번
        for j in range(i, n):
            if i % 3 == 0:      # 아래로
                x += 1
            elif i % 3 == 1:    # 위로
                y += 1
            else:               # 대각선 위로
                x -= 1
                y -= 1
            answer[x][y] = num
            num += 1
    
    result = []
    for ans in answer:
        result += ans
    return result