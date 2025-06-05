import sys

def main():
    input = sys.stdin.readline

    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    S = [[0] * (M+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, M+1):
            S[i][j] = A[i-1][j-1] + S[i-1][j] + S[i][j-1] - S[i-1][j-1]

    K = int(input())

    for _ in range(K):
        x1, y1, x2, y2 = map(int, input().split())
        result = (S[x2][y2] - S[x1-1][y2] - S[x2][y1-1] + S[x1-1][y1-1])

        print(result)

if __name__ == '__main__':
    main()