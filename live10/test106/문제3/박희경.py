def solution(m, n, puddles):
    graph = [[-1] * m for _ in range(n)]

    graph[0][0] = 1
    
    # 웅덩이 체크
    for x, y in puddles:
        graph[y - 1][x - 1] = 0

    # 첫 열 초기화 
    for i in range(1, n):
        if graph[i][0] == 0:
            graph[i][0] = 0
        else:
            graph[i][0] = graph[i - 1][0]

    # 첫 행 초기화
    for j in range(1, m):
        if graph[0][j] == 0:
            graph[0][j] = 0
        else:
            graph[0][j] = graph[0][j - 1]
            
    # 웅덩이 제외 경로 계산
    for i in range(1, n):
        for j in range(1, m):
            if graph[i][j] != 0:
                graph[i][j] = graph[i-1][j] + graph[i][j-1]
    
    return graph[n-1][m-1] % 1000000007