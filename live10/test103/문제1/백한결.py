def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                if A[j][i] and A[i][k]:
                    A[j][k] = 1

    for num in A:
        print(' '.join(map(str, num)))


if __name__ == "__main__":
    main()