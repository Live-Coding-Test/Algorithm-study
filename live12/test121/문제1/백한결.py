import sys

def main():
    input = sys.stdin.readline

    N, M, K = map(int, input().split())

    board = [input().strip() for _ in range(N)]

    w = [[0] * M for _ in range(N)]
    b = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            expectedColorIfWhite = 'W' if (i + j) % 2 == 0 else 'B'
            expectedColorIfBlack = 'B' if (i + j) % 2 == 0 else 'W'

            if board[i][j] != expectedColorIfWhite:
                w[i][j] = 1
            if board[i][j] != expectedColorIfBlack:
                b[i][j] = 1

    def prefixSum(array):
        ps = [[0] * (M+1) for _ in range(N+1)]

        for i in range(N):
            for j in range(M):
                ps[i+1][j+1] = array[i][j] + ps[i][j+1] + ps[i+1][j] - ps[i][j]

        return ps

    prefixSumWhite = prefixSum(w)
    print(prefixSumWhite)
    prefixSumBlack = prefixSum(b)
    print(prefixSumBlack)

    minRepaintCount = float('inf')
    for i in range(N - K + 1):
        for j in range(M - K + 1):
            x1, y1 = i, j
            x2, y2 = i + K, j + K
            whiteCount = prefixSumWhite[x2][y2] - prefixSumWhite[x1][y2] - prefixSumWhite[x2][y1] + prefixSumWhite[x1][y1]
            blackCount = prefixSumBlack[x2][y2] - prefixSumBlack[x1][y2] - prefixSumBlack[x2][y1] + prefixSumBlack[x1][y1]
            minRepaintCount = min(minRepaintCount, whiteCount, blackCount)

    print(minRepaintCount)

if __name__ == '__main__':
    main()