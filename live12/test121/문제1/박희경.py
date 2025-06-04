import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(str, input().rstrip())))

prefix_sum_black = [[0] * (m + 1) for _ in range(n + 1)]
prefix_sum_white = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(m):
        prefix_sum_black[i][j] = prefix_sum_black[i-1][j] + prefix_sum_black[i][j-1] - prefix_sum_black[i-1][j-1]
        prefix_sum_white[i][j] = prefix_sum_white[i-1][j] + prefix_sum_white[i][j-1] - prefix_sum_white[i-1][j-1] 
        if (i + j) % 2 == 0:
            if board[i][j] != 'B':
                # 바꿔야 함
                prefix_sum_black[i][j] += 1
        else:
            if board[i][j] == 'B':
                prefix_sum_white[i][j] += 1

count = float('inf')
for i in range(1, n - k + 2):
    for j in range(1, m  - k + 2):
        black_cnt = prefix_sum_black[i + k - 1][j + k - 1] - prefix_sum_black[i + k - 1][j - 1] - prefix_sum_black[i - 1][j + k - 1] + prefix_sum_black[i - 1][j - 1]
        white_cnt = prefix_sum_white[i + k - 1][j + k - 1] - prefix_sum_white[i + k - 1][j - 1] - prefix_sum_white[i - 1][j + k - 1] + prefix_sum_white[i - 1][j - 1]
        count = min(count, black_cnt, white_cnt)

print(count)