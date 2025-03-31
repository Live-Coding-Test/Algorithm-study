N = int(input())
result = 0

cols = [False] * N
diag1 = [False] * (2 * N - 1)
diag2 = [False] * (2 * N - 1)


def dfs(row):
    global result
    if row == N:
        result += 1
        return

    # row + col -> 오른쪽 아래 대각선
    # row - col + (N - 1) -> 왼쪽 아래 대각선
    for col in range(N):
        if cols[col] or diag1[row + col] or diag2[row - col + N - 1]:
            continue

        cols[col] = diag1[row + col] = diag2[row - col + N - 1] = True
        dfs(row + 1)
        # 백트래킹
        cols[col] = diag1[row + col] = diag2[row - col + N - 1] = False


dfs(0)
print(result)