import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(str, input().rstrip())))

cnt = []
for a in range(n - k + 1):
    for b in range(m - k + 1):
        white = 0
        black = 0 
        for i in range(a, a + k):
            for j in range(b, b + k):
                # 처음 색과 같아야 하는 부분
                if (i + j) % 2 == 0:
                    if board[i][j] != 'W':  
                        white += 1
                    else:
                        black += 1
                # 처음 색과 달라야 하는 부분
                else:
                    if board[i][j] != 'W':
                        black += 1
                    else:
                        white += 1
        cnt.append(white)
        cnt.append(black)
print(min(cnt))